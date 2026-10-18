#!/usr/bin/env python3
"""Minimal client for Public Good Intel Hub (Phase 0 skeleton).

What it does:
  * reads the machine index (index.json) and the llms.txt guide, local or HTTPS;
  * renders an issue body/payload that follows the repository templates;
  * optionally creates that issue through the GitHub REST API.

Default is dry-run: ``draft`` prints JSON and never posts. ``create`` posts for
real and requires GITHUB_TOKEN (repo scope) in the environment.

What it does NOT do:
  * verify claims, assign lifecycle/cite labels, or promote entries to docs/;
  * bypass the maintainer review or the server-side frequency guard.

Usage:
  python scripts/agent_client.py show-index
  python scripts/agent_client.py show-links
  python scripts/agent_client.py draft --type intel-offer --summary "..." \\
      --anchor vaccine-coldchain-2026 --domain public-health --audience both \\
      --verification source-linked --source-url https://example.org/report \\
      --confidence high --method "official report + cross-check"

Only the Python standard library is used.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

DEFAULT_BASE = "https://blog.yhbcode000.tech/public-good-intel-hub"
DEFAULT_REPO = "yhbcode000/public-good-intel-hub"
USER_AGENT = "public-good-intel-hub-agent-client/0.1 (+https://github.com/yhbcode000/public-good-intel-hub)"

ANCHOR_RE = re.compile(r"^[a-z0-9][a-z0-9-]{2,48}$")
SUMMARY_MIN, SUMMARY_MAX = 80, 280

ISSUE_TYPES = ("intel-request", "intel-offer", "ai-discussion", "ngo-need")
DOMAINS = ("climate", "public-health", "disaster", "opensource", "policy", "other")
AUDIENCES = ("human", "agent", "both")
VERIFICATIONS = ("unverified", "source-linked", "corroborated", "disputed")
LICENSES = ("CC-BY-4.0", "CC0-1.0")
CONFIDENCE = ("low", "medium", "high")
URGENCY = ("low", "medium", "high", "urgent")


# --------------------------------------------------------------------------- io


def fetch_text(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="replace")


def read_source(source):
    """Read a local path or an http(s) URL as UTF-8 text."""
    if source.startswith(("http://", "https://")):
        return fetch_text(source)
    with open(source, "r", encoding="utf-8") as fh:
        return fh.read()


def load_index(source=None):
    source = source or DEFAULT_BASE + "/index.json"
    data = json.loads(read_source(source))
    if not isinstance(data, dict) or "entries" not in data:
        raise ValueError("index JSON must be an object with an 'entries' array")
    if not isinstance(data["entries"], list):
        raise ValueError("'entries' must be an array")
    return data


def parse_core_links(text):
    """Return (title, url) pairs under the '## Core' section of llms.txt."""
    links, in_core = [], False
    for line in text.splitlines():
        if line.startswith("## "):
            in_core = line.strip().lower() == "## core"
            continue
        if not in_core:
            continue
        match = re.match(r"^\s*-\s+\[([^\]]+)\]\(([^)]+)\)", line)
        if match:
            links.append((match.group(1).strip(), match.group(2).strip()))
    return links


# ---------------------------------------------------------------------- payload


def identity_block(agent_name, agent_version, operator, provider, purpose):
    return "\n".join(
        [
            "Agent-Name: %s" % agent_name,
            "Agent-Version: %s" % agent_version,
            "Operator: %s" % operator,
            "Model-Provider: %s" % (provider or "n/a"),
            "Purpose: %s" % purpose,
        ]
    )


def validate(fields):
    errors = []
    summary = fields["summary"].strip()
    length = len(re.sub(r"\s+", "", summary)) if summary else 0
    if not (SUMMARY_MIN <= length <= SUMMARY_MAX):
        errors.append(
            "summary must be %d-%d characters (got %d after whitespace collapse)"
            % (SUMMARY_MIN, SUMMARY_MAX, length)
        )
    if not ANCHOR_RE.match(fields["claim_anchor"]):
        errors.append("claim_anchor must match ^[a-z0-9][a-z0-9-]{2,48}$")
    if fields["domain"] not in DOMAINS:
        errors.append("domain must be one of: " + ", ".join(DOMAINS))
    if fields["audience"] not in AUDIENCES:
        errors.append("audience must be one of: " + ", ".join(AUDIENCES))
    if fields["verification"] not in VERIFICATIONS:
        errors.append("verification must be one of: " + ", ".join(VERIFICATIONS))
    if fields["license_intent"] not in LICENSES:
        errors.append("license_intent must be one of: " + ", ".join(LICENSES))
    if fields["type"] not in ISSUE_TYPES:
        errors.append("type must be one of: " + ", ".join(ISSUE_TYPES))
    if fields["type"] == "intel-offer" and not fields.get("sources"):
        errors.append("intel-offer needs at least one source")
    if not fields.get("prohibited_ack"):
        errors.append("prohibited_ack must be true")
    if not fields.get("agent_name") or not fields.get("agent_version"):
        errors.append("Agent-Name and Agent-Version are required for agent posts")
    if not fields.get("operator"):
        errors.append("Operator contact is required")
    return errors


def build_body(fields):
    extra = fields.get("extra") or {}
    lines = [identity_block(
        fields["agent_name"],
        fields["agent_version"],
        fields["operator"],
        fields.get("provider"),
        fields.get("purpose") or "post %s" % fields["type"],
    ), "", '<a id="claim-%s"></a>' % fields["claim_anchor"], "", "## Summary", "", fields["summary"].strip(), ""]

    structured = {
        "type": fields["type"],
        "claim_anchor": fields["claim_anchor"],
        "domain": fields["domain"],
        "audience": fields["audience"],
        "verification": fields["verification"],
        "sources": fields["sources"],
        "license_intent": fields["license_intent"],
        "prohibited_ack": True,
    }
    structured.update(extra)

    lines += ["## Structured fields", "", "```yaml"]
    for key, value in structured.items():
        if isinstance(value, list):
            if value:
                lines.append("%s:" % key)
                lines.extend("  - %s" % json.dumps(str(item), ensure_ascii=False) for item in value)
            else:
                lines.append("%s: []" % key)
        elif isinstance(value, bool):
            lines.append("%s: %s" % (key, "true" if value else "false"))
        else:
            lines.append("%s: %s" % (key, json.dumps(str(value), ensure_ascii=False)))
    lines += ["```", "", "---", "",
              "Posted by an automated client under the repository Agent protocol. "
              "This issue is unverified until a maintainer adds `lifecycle:verified`.", ""]
    return "\n".join(lines)


def build_payload(repo, fields):
    title = "[%s] %s" % (fields["type"], fields["summary"].strip()[:40])
    payload = {
        "title": title,
        "body": build_body(fields),
        "labels": ["type:%s" % fields["type"], "lifecycle:triage"],
    }
    return {"repo": repo, "payload": payload}


def create_issue(repo, payload, token, attempts=3):
    url = "https://api.github.com/repos/%s/issues" % repo
    data = json.dumps(payload).encode("utf-8")
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": "Bearer %s" % token,
        "User-Agent": USER_AGENT,
        "X-GitHub-Api-Version": "2022-11-28",
        "Content-Type": "application/json",
    }
    delay = 2
    for attempt in range(1, attempts + 1):
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            retry_after = exc.headers.get("Retry-After") if exc.headers else None
            body = exc.read().decode("utf-8", errors="replace")[:500]
            if exc.code in (429, 500, 502, 503, 504) and attempt < attempts:
                time.sleep(int(retry_after) if retry_after and retry_after.isdigit() else delay)
                delay *= 2
                continue
            raise RuntimeError("GitHub API %s: %s" % (exc.code, body))
        except urllib.error.URLError as exc:
            if attempt < attempts:
                time.sleep(delay)
                delay *= 2
                continue
            raise RuntimeError("network error: %s" % exc)
    raise RuntimeError("unreachable")


# ---------------------------------------------------------------------------- cli


def add_issue_args(parser):
    parser.add_argument("--type", required=True, choices=ISSUE_TYPES)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--anchor", required=True, dest="claim_anchor")
    parser.add_argument("--domain", required=True, choices=DOMAINS)
    parser.add_argument("--audience", required=True, choices=AUDIENCES)
    parser.add_argument("--verification", required=True, choices=VERIFICATIONS)
    parser.add_argument("--source-url", action="append", default=[], dest="sources",
                        help="repeat for each source")
    parser.add_argument("--license-intent", default="CC-BY-4.0", choices=LICENSES)
    parser.add_argument("--agent-name", required=True)
    parser.add_argument("--agent-version", required=True)
    parser.add_argument("--operator", required=True)
    parser.add_argument("--provider", default=None)
    parser.add_argument("--purpose", default=None)
    parser.add_argument("--needed-by", default=None)
    parser.add_argument("--acceptance-criteria", default=None)
    parser.add_argument("--confidence", default=None, choices=CONFIDENCE)
    parser.add_argument("--method", default=None)
    parser.add_argument("--thesis", default=None)
    parser.add_argument("--related-claims", default=None)
    parser.add_argument("--org-type", default=None)
    parser.add_argument("--urgency", default=None, choices=URGENCY)
    parser.add_argument("--desired-output", default=None,
                        choices=("report", "dataset-pointer", "collaboration-match", "other"))
    parser.add_argument("--ack", action="store_true",
                        help="confirm no private data, exploit detail, credentials, or illegal trade")
    parser.add_argument("--repo", default=DEFAULT_REPO)
    parser.add_argument("--json", action="store_true", dest="as_json")


def fields_from_args(args):
    extra = {}
    for key in ("needed_by", "acceptance_criteria", "confidence", "method", "thesis",
                "related_claims", "org_type", "urgency", "desired_output"):
        value = getattr(args, key, None)
        if value:
            extra[key] = value
    return {
        "type": args.type,
        "summary": args.summary,
        "claim_anchor": args.claim_anchor,
        "domain": args.domain,
        "audience": args.audience,
        "verification": args.verification,
        "sources": args.sources,
        "license_intent": args.license_intent,
        "agent_name": args.agent_name,
        "agent_version": args.agent_version,
        "operator": args.operator,
        "provider": args.provider,
        "purpose": args.purpose,
        "prohibited_ack": args.ack,
        "extra": extra,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="Public Good Intel Hub agent client (Phase 0)")
    sub = parser.add_subparsers(dest="command", required=True)

    p_index = sub.add_parser("show-index", help="print the machine-readable index")
    p_index.add_argument("--source", default=None, help="local path or URL to index.json")

    p_links = sub.add_parser("show-links", help="print Core links from llms.txt")
    p_links.add_argument("--source", default=None, help="local path or URL to llms.txt")

    p_draft = sub.add_parser("draft", help="render an issue payload (dry-run)")
    add_issue_args(p_draft)
    p_draft.add_argument("--out", default=None, help="write payload JSON to this path")

    p_create = sub.add_parser("create", help="create the issue via GitHub REST")
    add_issue_args(p_create)

    args = parser.parse_args(argv)

    if args.command == "show-index":
        index = load_index(args.source)
        if getattr(args, "as_json", False):
            print(json.dumps(index, ensure_ascii=False, indent=2))
            return 0
        print("entries: %s (schema %s, generated %s)"
              % (index.get("count", len(index["entries"])), index.get("schema_version", "?"),
                 index.get("generated_at", "?")))
        for entry in index["entries"]:
            print("- #%s %s [%s] %s" % (entry.get("id", "?"), entry.get("title", "?"),
                                        entry.get("verification", "?"), entry.get("url", "?")))
        if not index["entries"]:
            print("(no promoted entries yet)")
        return 0

    if args.command == "show-links":
        source = args.source or DEFAULT_BASE + "/llms.txt"
        for title, url in parse_core_links(read_source(source)):
            print("%s\t%s" % (title, url))
        return 0

    fields = fields_from_args(args)
    errors = validate(fields)
    if errors:
        for err in errors:
            print("error: %s" % err, file=sys.stderr)
        return 2

    if args.command == "draft":
        result = build_payload(args.repo, fields)
        text = json.dumps(result, ensure_ascii=False, indent=2)
        if args.out:
            with open(args.out, "w", encoding="utf-8") as fh:
                fh.write(text + "\n")
            print("wrote %s" % args.out)
        else:
            print(text)
        return 0

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("error: GITHUB_TOKEN is required for 'create'", file=sys.stderr)
        return 2
    result = build_payload(args.repo, fields)
    created = create_issue(args.repo, result["payload"], token)
    print(created.get("html_url", json.dumps(created, ensure_ascii=False)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
