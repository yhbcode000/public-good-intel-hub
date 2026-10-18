# What We Index

The Verified Index is the static, citable layer of Public Good Intel Hub. This page states exactly what enters it, what never enters it, and how to tell an entry's status from its URL and fields.

## 1. What the index is

A maintained list of conclusions promoted from GitHub Issues. Each entry has:

- a stable URL under `/citations/`;
- a standalone summary;
- at least one parseable source;
- a verification level assigned or confirmed by a maintainer;
- a link back to the source issue and the claim anchor;
- a license and an `updated` date.

It is not a search engine, a news feed, a dataset repository, or a mirror of issue comments.

## 2. Inclusion criteria

All must hold:

1. The claim is within scope: a social problem arising from large-scale AI deployment, or a public-good fact needed to reason about one.
2. The source issue has `lifecycle:verified` and `cite:ready`.
3. The summary is 80-280 characters, standalone, and free of context-dependent references.
4. At least one source is publicly reachable and supports the specific claim, or a maintainer exemption for a public literature reference is recorded.
5. The verification level is `source-linked` or `corroborated`.
6. The claim anchor is stable and unique.
7. Prohibited-content checks pass.
8. The claim is not a near-duplicate of an existing entry.

## 3. Exclusion criteria

Never indexed:

- identifiable personal data, medical records, or precise location traces;
- undisclosed vulnerabilities, exploit chains, proofs of concept, or attack instructions;
- credentials, keys, session tokens, or database dumps;
- offers to trade or methods to obtain illegal data;
- claims whose only support is an unverifiable screenshot, an anonymous rumor, or a circular citation;
- paid placements, "AI mention" guarantees, and keyword-matrix pages;
- automatic mirrors of issue threads.

## 4. Domains

Entries carry one domain label:

| Domain | Scope |
| --- | --- |
| `climate` | Climate, energy, and environmental public-good claims |
| `public-health` | Health systems, access, and public-health information |
| `disaster` | Disaster response, hazard data, and recovery |
| `opensource` | Open-source tooling, data, and governance |
| `policy` | Rules, standards, procurement, and public decision-making |
| `other` | Public-good claims outside the above |

## 5. Audience

| Value | Meaning |
| --- | --- |
| `human` | Written primarily for people |
| `agent` | Written primarily for machine consumption |
| `both` | Suitable for both |

Audience describes presentation, not trust. `agent` entries are not more authoritative than `human` entries.

## 6. Evidence tiers

| Tier | What it means | Eligible |
| --- | --- | --- |
| No usable source | Claim only | No |
| One public source | `source-linked`; checkable but not cross-checked | Yes, after review |
| Independent corroboration | `corroborated`; two or more independent sources | Yes |
| Disputed | Substantive unresolved challenge | Page remains, marked needs review |
| Retracted | Illegal content, private data, credentials, or forged source | Explanatory page only |

## 7. Entry states

| State | Visible signal | How to treat it |
| --- | --- | --- |
| Promoted | Entry exists in `/citations/` and `index.json` | Citable with access date |
| Disputed | Needs-review banner; `lifecycle:disputed` on the source issue | Cite with "as of {date}, disputed" |
| Retracted | Explanatory page at the same URL | Do not cite as a conclusion; cite the explanation |
| Absent | No entry | Not citable; use the issue only as a lead |

## 8. What is explicitly not indexed

- Opinions without sources, even when widely shared.
- Forecasts presented as facts; forecasts may be discussed in issues but not promoted as conclusions.
- Anything requiring access to private systems to verify.
- Content that identifies a person who has not consented to public attention.
- Content whose publication would create a safety risk.

## 9. Non-goals

- Maximizing the number of entries. An empty index is acceptable; a polluted one is not.
- Ranking by popularity, stars, or engagement.
- Replacing peer review, journalism, or official statistics. The index points to evidence; it does not certify truth beyond its stated verification level.
- Guaranteeing citation by any search or generative engine.

## 10. Checking an entry's status

1. Open the entry URL under `/citations/`.
2. Read `verification`, `verified_at`, and `updated`.
3. Check for a needs-review or retraction banner.
4. Follow `source_issue` and confirm the issue still carries `lifecycle:verified` and `cite:ready`.
5. If the page and `index.json` disagree, trust the page with the newer `updated` and report the discrepancy in the source issue.

See the [citation policy](./citation-policy.md) for citation formats and the [methodology](./methodology.md) for the promotion checklist.
