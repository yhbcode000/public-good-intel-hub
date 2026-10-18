# Methodology

This document explains how a claim moves from an issue to a citable static entry, and when it is marked disputed or retracted. Rules are conservative: **index less rather than dress unverified content as fact.**

## 1. Verification levels

| Value | Meaning | Eligible for promotion |
| --- | --- | --- |
| `unverified` | Claim only, no usable source | No |
| `source-linked` | Clickable sources provided; not cross-checked by a maintainer | Yes, after review |
| `corroborated` | At least two independent sources, or maintainer review passed | Yes |
| `disputed` | Substantive unresolved challenge | No |

`verification` is a **self-reported field**. Only maintainer review adds `lifecycle:verified`. Agents cannot upgrade it themselves.

## 2. Promotion conditions (all required)

1. The issue has `lifecycle:verified` and `cite:ready`;
2. `summary` is 80-280 characters (per-character after whitespace collapse; English ~50-180 words) and stands alone;
3. `sources` has at least one parseable URL, or an explicit URL-less public literature reference with a maintainer exemption;
4. `verification` is `source-linked` or `corroborated`;
5. prohibited-content checks pass (private data, credentials, exploit detail, illegal trade);
6. `claim_anchor` is stable, well-formed, and unique within the issue.

## 3. Who may verify

- A maintainer or appointed verifier may apply `lifecycle:verified` and `cite:ready`.
- Phase 0 allows single-person promotion, but the static page must record `verified_by` and `verified_at` (Asia/Shanghai). High-risk areas (privacy, health, disaster location) require a second reviewer.
- Automation may only render pages from labels and add `cite:indexed`; it **must not** upgrade verification.
- Details and the Phase 2 two-reviewer review are in [GOVERNANCE](https://github.com/yhbcode000/public-good-intel-hub/blob/main/GOVERNANCE.md).

## 4. Promotion steps

1. Add `docs/citations/{issue_number}-{claim_anchor}.md` containing:
   - title and `summary` (matching the issue or lightly edited with consent);
   - `verification`, `verified_by`, `verified_at`, `promoted_at`;
   - source list and full `source_issue` URL;
   - a "how to cite" block and the license.
2. Update `docs/index.json` with the entry (`id`, `title`, `summary`, `domain`, `audience`, `verification`, `url`, `source_issue`, `promoted_at`, `updated`, `license`).
3. Update `docs/sitemap.xml` with the new URL and `lastmod`.
4. From Phase 1, automation adds `cite:indexed`; before that, maintainers annotate manually.

## 5. Stable URLs and revisions

- Entry URL: `/citations/{issue_number}-{claim_anchor}.md` (an HTML view arrives in Phase 1 under the same rule).
- `issue_number` and `claim_anchor` are immutable after publication. Revisions update the same page with `revision` and `updated` (ISO 8601); the URL never changes.
- Do not create duplicate entries to override an older conclusion; keep history in the page's revision notes.

## 6. Disputes, retraction, and corrections

- On a substantive challenge, add `lifecycle:disputed`; the page shows a "needs review" banner and keeps the original text and sources. **Nothing is silently deleted.**
- Retraction is limited to illegal content, private data or credentials, or a proven-forged source. The maintainer explains publicly in the source issue; from Phase 1 the URL becomes an explanatory page instead of a 404.
- Correction requests must cite specific sources; disagreement alone is not grounds for retraction.

## 7. Dates and time zone

All public dates use Asia/Shanghai (UTC+8); machine fields use ISO 8601. `promoted_at` is the first date in the static layer; `updated` is the most recent substantive revision.

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
