#!/usr/bin/env python3
"""Generate Atom and RSS feeds of promoted Verified Index entries from docs/index.json.

Empty feeds are valid when the index has no entries yet. Run from repo root:
  python3 scripts/generate_feeds.py
"""
from __future__ import annotations

import html
import json
import pathlib
from datetime import datetime, timezone
from xml.sax.saxutils import escape

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
INDEX = DOCS / "index.json"
ATOM = DOCS / "atom.xml"
RSS = DOCS / "rss.xml"
HOME = "https://blog.yhbcode000.tech/public-good-intel-hub/"
REPO = "https://github.com/yhbcode000/public-good-intel-hub"


def rfc3339(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def rfc822(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")


def entry_updated(entry: dict, fallback: datetime) -> datetime:
    for key in ("updated", "promoted_at", "published"):
        raw = entry.get(key)
        if not raw:
            continue
        try:
            return datetime.fromisoformat(str(raw).replace("Z", "+00:00")).astimezone(timezone.utc)
        except ValueError:
            continue
    return fallback


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    entries = list(data.get("entries") or [])
    generated = data.get("generated_at") or datetime.now(timezone.utc).date().isoformat()
    try:
        feed_updated = datetime.fromisoformat(str(generated)).replace(tzinfo=timezone.utc)
    except ValueError:
        feed_updated = datetime.now(timezone.utc)
    if entries:
        feed_updated = max(entry_updated(e, feed_updated) for e in entries)

    title = data.get("name") or "Public Good Intel Hub"
    subtitle = data.get("description") or "Verified public-good intelligence conclusions."

    # --- Atom ---
    atom_items = []
    for e in entries:
        eid = escape(str(e.get("id") or e.get("url") or ""))
        etitle = escape(str(e.get("title") or eid))
        eurl = escape(str(e.get("url") or (HOME + "citations/")))
        summary = escape(str(e.get("summary") or e.get("description") or ""))
        updated = rfc3339(entry_updated(e, feed_updated))
        atom_items.append(
            f"""  <entry>
    <title>{etitle}</title>
    <link href="{eurl}" rel="alternate" type="text/html"/>
    <id>{eid}</id>
    <updated>{updated}</updated>
    <summary>{summary}</summary>
  </entry>"""
        )
    atom = f"""<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <title>{escape(title)} — Verified Index</title>
  <subtitle>{escape(subtitle)}</subtitle>
  <link href="{HOME}atom.xml" rel="self" type="application/atom+xml"/>
  <link href="{HOME}" rel="alternate" type="text/html"/>
  <link href="{HOME}index.json" rel="related" type="application/json"/>
  <id>{HOME}atom.xml</id>
  <updated>{rfc3339(feed_updated)}</updated>
  <author>
    <name>Public Good Intel Hub</name>
    <uri>{REPO}</uri>
  </author>
  <rights>CC-BY-4.0</rights>
{chr(10).join(atom_items)}
</feed>
"""
    ATOM.write_text(atom, encoding="utf-8", newline="\n")

    # --- RSS 2.0 ---
    rss_items = []
    for e in entries:
        etitle = escape(str(e.get("title") or e.get("id") or ""))
        eurl = escape(str(e.get("url") or HOME))
        summary = escape(str(e.get("summary") or e.get("description") or ""))
        guid = escape(str(e.get("id") or eurl))
        pub = rfc822(entry_updated(e, feed_updated))
        rss_items.append(
            f"""    <item>
      <title>{etitle}</title>
      <link>{eurl}</link>
      <guid isPermaLink="false">{guid}</guid>
      <pubDate>{pub}</pubDate>
      <description>{summary}</description>
    </item>"""
        )
    rss = f"""<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{escape(title)} — Verified Index</title>
    <link>{HOME}</link>
    <description>{escape(subtitle)}</description>
    <language>en</language>
    <lastBuildDate>{rfc822(feed_updated)}</lastBuildDate>
    <atom:link href="{HOME}rss.xml" rel="self" type="application/rss+xml"/>
    <docs>{HOME}citation-policy.md</docs>
{chr(10).join(rss_items)}
  </channel>
</rss>
"""
    RSS.write_text(rss, encoding="utf-8", newline="\n")
    print(f"wrote {ATOM.relative_to(ROOT)} and {RSS.relative_to(ROOT)} ({len(entries)} entries)")


if __name__ == "__main__":
    main()
