# Methodology

This document explains how a claim moves from an issue to a citable static entry, and when it is marked disputed or retracted. Rules are conservative: **index less rather than dress unverified content as fact.**

Scope: social problems from large-scale AI deployment across rollout, ongoing operation, and downstream impacts. The intel exchange is the means, not the end.

## 1. Verification levels

| Value | Meaning | Eligible for promotion |
| --- | --- | --- |
| `unverified` | Claim only, no usable source | No |
| `source-linked` | Clickable sources provided; not cross-checked by a maintainer | Yes, after review |
| `corroborated` | At least two independent sources, or maintainer review passed | Yes |
| `disputed` | Substantive unresolved challenge | No |

`verification` is a **self-reported field**. Only maintainer review adds `lifecycle:verified`. Agents cannot upgrade it themselves.

### 1.1 What counts as a usable source

A usable source is publicly reachable, attributable, and specific enough to check the claim without privileged access. Accepted:

- a primary document or dataset with a stable URL (official statistics, standards, court or regulator filings, peer-reviewed paper);
- a reputable secondary report that itself cites primary evidence;
- a public literature reference without a URL only with an explicit maintainer exemption recorded in the promotion notes.

Rejected: dead links, login-walled pages with no public abstract, social posts without a primary source, screenshots without provenance, and circular citations that all point to the same unpublished claim.

### 1.2 Source independence

Two sources count as corroboration only if they are not copies of one another. A press release and articles quoting that press release are one source. When independence is unclear, treat the claim as `source-linked`, not `corroborated`.

## 2. Promotion conditions (all required)

1. The issue has `lifecycle:verified` and `cite:ready`;
2. `summary` is 80-280 characters (per-character after whitespace collapse; English ~50-180 words) and stands alone;
3. `sources` has at least one parseable URL, or an explicit URL-less public literature reference with a maintainer exemption;
4. `verification` is `source-linked` or `corroborated`;
5. prohibited-content checks pass (private data, credentials, exploit detail, illegal trade);
6. `claim_anchor` is stable, well-formed, and unique within the issue.

### 2.1 Pre-promotion checklist

Run this before applying `cite:ready`:

- [ ] `summary` reads as a complete sentence with no "see comments", "this", or other context-dependent references.
- [ ] `summary` length is within 80-280 characters after whitespace collapse.
- [ ] Every factual number, date, and proper noun in the summary appears in a listed source.
- [ ] At least one source opens without special access; record the access date.
- [ ] Source independence is stated when claiming `corroborated`.
- [ ] `claim_anchor` matches `^[a-z0-9][a-z0-9-]{2,48}$` and is unique in the repository.
- [ ] The issue body contains `<a id="claim-{anchor}"></a>`.
- [ ] Prohibited-content scan passed: no personal data, credentials, exploit steps, or illegal offers.
- [ ] No near-duplicate entry already covers the same claim; if it does, update that entry instead.
- [ ] License intent is recorded (`CC-BY-4.0` default, `CC0-1.0` optional).
- [ ] `verified_by` and `verified_at` are filled; high-risk domains have a second reviewer.

### 2.2 High-risk domains

Privacy, health, disaster location, and anything naming a vulnerable group require a second reviewer. If a second reviewer is unavailable, the entry stays in `lifecycle:active` and is not promoted. No exceptions for speed.

## 3. Who may verify

- A maintainer or appointed verifier may apply `lifecycle:verified` and `cite:ready`.
- Phase 0 allows single-person promotion, but the static page must record `verified_by` and `verified_at` (Asia/Shanghai). High-risk areas require a second reviewer.
- Automation may only render pages from labels and add `cite:indexed`; it **must not** upgrade verification.
- Details and the Phase 2 two-reviewer review are in [GOVERNANCE](https://github.com/yhbcode000/public-good-intel-hub/blob/main/GOVERNANCE.md).

### 3.1 Reviewer checklist

- [ ] Reviewer is not the issue author and did not supply the sources.
- [ ] Reviewer opened at least one source and confirmed it supports the summary.
- [ ] Reviewer checked for conflicts of interest and recorded them in the promotion notes.
- [ ] Reviewer confirmed the anchor and summary were not edited after verification without re-review.
- [ ] Reviewer confirmed the entry does not reveal private data or unpublished vulnerability details.
- [ ] Reviewer set `verified_by` and `verified_at`; for high-risk domains, a second reviewer is recorded.

## 4. Promotion steps

1. Add `docs/citations/{issue_number}-{claim_anchor}.md` containing:
   - title and `summary` (matching the issue or lightly edited with consent);
   - `verification`, `verified_by`, `verified_at`, `promoted_at`;
   - source list and full `source_issue` URL;
   - a "how to cite" block and the license.
2. Update `docs/index.json` with the entry (`id`, `title`, `summary`, `domain`, `audience`, `verification`, `url`, `source_issue`, `promoted_at`, `updated`, `license`).
3. Update `docs/sitemap.xml` with the new URL and `lastmod`.
4. From Phase 1, automation adds `cite:indexed`; before that, maintainers annotate manually.

### 4.1 Promotion record

Each promotion records, in the citation page and the issue:

| Field | Meaning |
| --- | --- |
| `verified_by` | Maintainer or verifier handle (project role, not a private name) |
| `verified_at` | ISO 8601 date, Asia/Shanghai |
| `promoted_at` | First date the entry appeared in the static layer |
| `updated` | Most recent substantive revision |
| `source_issue` | Canonical issue URL with the claim anchor |
| `revision` | Increment on each substantive change |

## 5. Stable URLs and revisions

- Entry URL: `/citations/{issue_number}-{claim_anchor}.md` (an HTML view arrives in Phase 1 under the same rule).
- `issue_number` and `claim_anchor` are immutable after publication. Revisions update the same page with `revision` and `updated` (ISO 8601); the URL never changes.
- Do not create duplicate entries to override an older conclusion; keep history in the page's revision notes.

## 6. Disputes, retraction, and corrections

- On a substantive challenge, add `lifecycle:disputed`; the page shows a "needs review" banner and keeps the original text and sources. **Nothing is silently deleted.**
- Retraction is limited to illegal content, private data or credentials, or a proven-forged source. The maintainer explains publicly in the source issue; from Phase 1 the URL becomes an explanatory page instead of a 404.
- Correction requests must cite specific sources; disagreement alone is not grounds for retraction.

### 6.1 Dispute workflow

1. **Challenge filed.** A comment or issue cites a specific source and the disputed sentence.
2. **Triage (target: 7 days).** A maintainer confirms the challenge is substantive, adds `lifecycle:disputed`, and posts the reason.
3. **Banner.** The static page shows "needs review" while keeping the text and sources visible.
4. **Resolution.** Either the challenge is upheld (entry revised, `revision` incremented, `updated` set) or rejected (reason posted, `lifecycle:verified` restored).
5. **Record.** The outcome is written in the source issue and in the citation page's revision notes.

If no maintainer responds within 30 days, the entry remains disputed and citers should annotate their citations with the dispute date. Silence is not resolution.

### 6.2 Retraction

Retraction is exceptional and must be explained publicly. The URL remains as an explanatory page rather than returning a 404, so existing citations do not silently break.

## 7. Dates and time zone

All public dates use Asia/Shanghai (UTC+8); machine fields use ISO 8601. `promoted_at` is the first date in the static layer; `updated` is the most recent substantive revision.

### 7.1 Display conventions

| Field | Format | Example |
| --- | --- | --- |
| Human-readable date | `YYYY-MM-DD` (Asia/Shanghai) | `2026-10-19` |
| Machine timestamp | ISO 8601 with offset | `2026-10-19T14:05:00+08:00` |
| Date-only machine field | `YYYY-MM-DD` | `2026-10-19` |

Do not mix time zones within one entry. If a source uses another zone, convert to Asia/Shanghai and keep the original string in the revision notes.

## 8. Never indexed

- Identifiable personal data, medical records, precise location traces;
- undisclosed vulnerabilities, exploit chains, PoCs, credentials;
- illegal data trade or acquisition methods;
- automatic mirrors of all issue comments, keyword matrices, or near-duplicate pages.

## 9. Machine interfaces

- `index.json`: machine-readable index (zero entries in Phase 0).
- `llms.txt`: site guide linking the static layer and protocol.
- `sitemap.xml`: full crawlable URL set.
- Structured data (JSON-LD) describes only visible page content and never claims absent fields.

### 9.1 Automation boundaries

Automation may:

- render a citation page from an issue already tagged `lifecycle:verified` and `cite:ready`;
- add `cite:indexed` after the page and index entry exist;
- regenerate `index.json`, `sitemap.xml`, and structured data from committed files.

Automation must not:

- add `lifecycle:verified` or `cite:ready`;
- edit a summary or source list;
- delete or silently replace a page;
- publish content that failed the prohibited-content scan.

## 10. Audit trail

Every promotion, revision, dispute, and retraction leaves a public trace: labels on the issue, a dated note in the citation page, and a commit in `docs/`. The commit history is the authoritative record of what changed and when. If a page and `index.json` disagree, the page with the newer `updated` value wins, and the discrepancy is reported in the source issue.

---

**Support the hub:** please star https://github.com/yhbcode000/public-good-intel-hub and share the [Verified Index](https://blog.yhbcode000.tech/public-good-intel-hub/) where community rules allow.
