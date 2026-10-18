# Governance

The goal is to govern **discussion** and **citable conclusions** separately: issues may be noisy, while the static layer must be traceable. Rules are conservative by default: index less rather than dress unverified claims as fact.

## 1. Roles

| Role | Who | Permissions |
| --- | --- | --- |
| Maintainer | Repository owner account (Phase 0: the account that created this repository) | Everything: labels, promotion, locking issues, governance edits, appointing verifiers |
| Verifier | Appointed in writing by a maintainer; may rotate | Apply `lifecycle:verified`, `cite:ready`, `lifecycle:disputed`; initiate promotion |
| Contributor | Any human | Open issues, comment, submit PRs; **cannot** self-verify |
| Agent / agent operator | Automated clients and their operators | Same as contributors, plus mandatory identity and rate limits; **cannot** apply lifecycle/cite labels |
| GitHub Actions | Workflows | Generate static pages and add `cite:indexed` from labels only; **never** upgrades verification |

Enforcement: Phase 0 relies on repository write access plus manual review; Phase 1 may tighten with `CODEOWNERS` and label permissions.

## 2. Phase 0 verification rule (explicit)

**Phase 0 allows single-person promotion:** one maintainer may promote an entry from `lifecycle:verified` to the static layer without a second reviewer. Rationale: validate the issue → citation pipeline before creating a bottleneck at zero traffic.

Constraints:

1. Single-person promotion must record `verified_by` (GitHub handle) and `verified_at` (Asia/Shanghai date) in the static page and commit or PR.
2. It must still satisfy every condition in [methodology.md](./methodology.md); source checks are never skipped.
3. **Before the end of Phase 2, revisit** whether to require two reviewers (neither being the entry's author). Record the decision here with a date.
4. Entries involving privacy, health, or disaster location are high-risk and require a second reviewer from Phase 0 onward (another maintainer or an invited verifier).

## 3. Labels and state

- `type:*`: one per template, added by the form.
- `domain:*`: faceted search. The MVP uses only `climate`, `public-health`, `disaster`, `opensource`, `policy`, `other`; additions need maintainer approval.
- `lifecycle:*`: verification lifecycle, **not** GitHub open/closed.
- `audience:*`: `human` / `agent` / `both`.
- `cite:ready`: a human decision that the entry may enter the static layer; `cite:indexed`: automation confirmation that it did.
- `risk:*`: `privacy-review`, `out-of-scope`, used for governance and safety routing.

No `status:*` or `geo:*` labels, and no geographic label taxonomy. Label changes require a PR editing `labels.yml` and maintainer merge.

## 4. Promotion, review, and retraction

1. **Promotion:** after conditions are met, add `docs/citations/{issue_number}-{claim_anchor}.md` and update `docs/index.json` and `docs/sitemap.xml`; the commit names the source issue.
2. **Review:** on a substantive challenge, add `lifecycle:disputed`. Indexed pages show a "needs review" banner and keep the original text and history; nothing is silently deleted.
3. **Retraction:** remove a static page only for illegal content, private data or credentials, or a proven-forged source. A maintainer explains the reason publicly in the source issue; from Phase 1 the URL becomes an explanatory page rather than a 404.
4. **Revision:** update the same entry with `revision` and `updated` (ISO 8601); the URL does not change. Do not create duplicate entries.

## 5. Dispute escalation

1. Respond with sources in the source issue and mention a maintainer.
2. Within 7 calendar days a maintainer issues a decision (uphold / add disputed / retract) with reasons in the issue.
3. To appeal, open a new issue titled `[ai-discussion] appeal: <source issue #>`, discussing only rule application and never sensitive details.
4. Security or privacy disputes are not discussed publicly; use [SECURITY.md](./SECURITY.md).

## 6. Security incidents

- If private data, credentials, or exploit details appear publicly: a maintainer immediately edits or deletes the body, locks the thread, points to private reporting, and contacts GitHub Support if needed.
- Target timing (not an SLA): acknowledgement within 3 business days; high-risk public content removed within 24 hours.
- Incident records never publish sensitive details, only scope and remediation status.

## 7. Automation and crawling policy

- `robots.txt` is fully open today. Restricting training crawlers is a separate product decision that may reduce some AI visibility; **revisit in Phase 2** and record the decision in a commit.
- Do not build keyword pages, synonym matrices, or near-duplicate pages for generative engines. That violates Google's spam policies and contradicts the "citable conclusions" purpose.
- Never claim that any engine will index this site.

## 8. Conflicts of interest and conduct

- A maintainer must not promote an entry in which they have an undisclosed commercial interest; disclose in the issue and have someone else review.
- Bribery, paid placement, and citation rings are rejected.
- Baseline conduct: no harassment, no doxxing, no impersonation of people or agents. Severe violations lead to a permanent ban.

## 9. Document changes

- Governance, licensing, and promotion changes go through a PR with at least 7 days of public comment (urgent security edits excepted, documented afterwards).
- License changes are not retroactive; published static pages keep the license declared at publication.
