# Citation Policy

The static layer (this Pages site and `/citations/`) is the only authoritative, citable statement layer. Issues and comments are evidence only.

## 1. What may be cited

- Entries under `docs/citations/` (none yet in Phase 0);
- conclusions promoted by maintainers whose pages declare `verification: source-linked` or `corroborated`.

**Do not** treat issue links, issue comments, or unpromoted `summary` text as formal citations. An issue's open/closed state only reflects discussion, not verification.

## 2. URL conventions

| Resource | URL |
| --- | --- |
| Home / human index | `https://yhbcode000.github.io/public-good-intel-hub/` |
| Machine index | `https://yhbcode000.github.io/public-good-intel-hub/index.json` |
| Single citation | `https://yhbcode000.github.io/public-good-intel-hub/citations/{issue_number}-{claim_anchor}.md` |
| Source issue | `https://github.com/yhbcode000/public-good-intel-hub/issues/{issue_number}#claim-{claim_anchor}` |
| Method and rules | `/methodology.md`, `/citation-policy.md`, `/faq.md` |
| Agent guide | `/llms.txt` |

`issue_number` and `claim_anchor` never change after publication. Revisions update the same URL and mark `updated`.

## 3. Citation formats

For a single conclusion:

```text
Public Good Intel Hub. "<Title>" (claim: {claim_anchor}, issue #{issue_number}).
Verified {verification}; promoted {promoted_at}. Accessed {YYYY-MM-DD}.
https://yhbcode000.github.io/public-good-intel-hub/citations/{issue_number}-{claim_anchor}.md
```

When quoting a summary fragment, keep the anchor and URL, do not rewrite in a way that changes meaning, and do not omit the `verification` level.

## 4. Fields to preserve

| Field | Source |
| --- | --- |
| Title / `summary` | Citation page |
| `verification` | Citation page (self-report is not review; the page shows the final level) |
| `promoted_at` / `updated` | Citation page (Asia/Shanghai) |
| `source_issue` | Citation page |
| License | Page footer (default CC-BY-4.0; per-entry CC0 exception) |
| Access date | Added by the citer |

## 5. Machine reading

- Prefer `index.json` with fields `id`, `title`, `summary`, `domain`, `audience`, `verification`, `url`, `source_issue`, `promoted_at`, `updated`, `license`.
- `index.json` and static pages share a source. If they conflict, the page with the newer `updated` wins; report the discrepancy.
- `sitemap.xml` is for discovery only and does not imply verification.

## 6. Corrections and retractions

- For factual errors, provide verifiable sources in the source issue or a new issue and mention a maintainer; they will add `lifecycle:disputed` and show a "needs review" banner.
- Entries are not deleted over disagreement. Only illegal content, private data or credentials, or forged sources trigger retraction, with a public explanation.
- If you cited an entry later marked disputed, annotate your citation with "as of {date}, disputed" and link the page.

## 7. License and redistribution

- Documentation and static conclusions default to **CC-BY-4.0**: redistribution and adaptation are allowed with attribution, a license link, and an indication of changes.
- Code is **Apache-2.0**.
- If an entry declares CC0-1.0, that page governs.
- Repository metadata: [CITATION.cff](https://github.com/yhbcode000/public-good-intel-hub/blob/main/CITATION.cff).

## 8. No guarantees

This site does not guarantee indexing by any generative engine, search engine, or dataset. Verify sources and recency before citing.
