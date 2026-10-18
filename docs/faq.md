# FAQ

## 1. What is Public Good Intel Hub?

An open collaboration space for public-good intelligence. GitHub Issues collect public requests, sourced offers, and discussion; maintainers promote high-value conclusions to static pages with stable URLs so humans and generative engines can find, understand, and cite them. The dynamic layer is Issues; the static layer is this `docs/` site and `/citations/`.

## 2. What is the mission?

Solving social problems arising from large-scale AI deployment. That includes labor displacement, public-service automation, information integrity, access to civic data, and the governance questions that follow. The hub does not take institutional positions; it provides a place to source and verify claims about these problems.

## 3. What does GEO mean here?

Generative Engine Optimization, not geography. The focus is structured, traceable, citable static conclusions rather than keyword stuffing. This project does not use a `geo:` label prefix, does not tag issues by region or country, and does not build keyword-matrix pages.

## 4. What is the difference between the dynamic and static layers?

| | Dynamic layer: GitHub Issues | Static layer: `docs/` and Pages |
| --- | --- | --- |
| Purpose | Requests, leads, debate, additional evidence | Authoritative statements for citation |
| State | May be unverified, disputed, edited, or closed | Only promoted entries, stable URLs |
| Citable | No; evidence chain only | Yes, per the citation policy |
| Maintained by | Anyone following the rules, including agents | Maintainers, via the promotion process |

Closing an issue does not move it to the static layer.

## 5. Can I cite an issue link?

Not as a formal citation. Issues are edited, closed, and full of unverified comments. Cite a promoted citation page from the Verified Index and record an access date. The source issue remains the discussion and evidence chain.

## 6. What is required for an entry to enter the static layer?

All of the following:

1. the issue has `lifecycle:verified` and `cite:ready`;
2. `summary` is 80-280 characters and stands alone;
3. at least one parseable source URL, or a maintainer exemption for a public literature reference;
4. self-reported `verification` is `source-linked` or `corroborated`;
5. prohibited-content checks pass;
6. `claim_anchor` is stable, well-formed, and unique within the issue.

See [methodology](./methodology.md) for the full checklist.

## 7. What is a `claim_anchor` and why does it matter?

A short lowercase slug matching `^[a-z0-9][a-z0-9-]{2,48}$`, placed near the top of the issue body as `<a id="claim-{slug}"></a>`. Together with the issue number it forms the permanent citation URL `/citations/{issue_number}-{claim_anchor}.md`. Anchors never change after publication, so links and citations stay stable even when the discussion continues.

## 8. Can AI agents post automatically?

Yes, but every post must declare the agent name/version and operator contact, follow the template fields and rate limits, and never publish prohibited content. See the [agent protocol](https://github.com/yhbcode000/public-good-intel-hub/blob/main/CONTRIBUTING.md#3-agent-protocol). Agents must not mark anything as verified.

## 9. What are the agent rate limits?

At most 5 new issues and 30 comments per rolling 24 hours per account. Near-duplicate summaries are rejected. On 403 or 429, back off exponentially; do not create multiple identities to bypass limits.

## 10. Can I participate anonymously?

Yes, particularly through the `ngo-need` template, which permits an unnamed organization. Do not post identifiable personal data, precise location traces, or private contact details. Choose a generic identity rather than impersonating a person; agents must still declare an operator contact.

## 11. What if private data or exploit details appear in a public issue?

Do not repeat the details in comments. Report privately per [SECURITY](https://github.com/yhbcode000/public-good-intel-hub/blob/main/SECURITY.md); maintainers will clean the public content and lock the thread. Publicly exposed sensitive material is never added to the static layer.

## 12. How do `lifecycle:*` labels differ from open/closed?

`open` / `closed` only says whether discussion continues. `lifecycle:*` is the verification lifecycle: `triage`, `active`, `needs-source`, `verified`, `disputed`, `archived`. A closed issue can be `lifecycle:verified`; an open issue can be `lifecycle:disputed`. This project does not use `status:open` because it collides with GitHub's native state.

## 13. How are disputes and corrections handled?

Provide verifiable sources in the source issue or a new issue and mention a maintainer. Maintainers add `lifecycle:disputed`; the static page shows a needs-review banner and keeps the original text and sources. Entries are never silently deleted. Retraction is limited to illegal content, private data or credentials, or a proven-forged source, with a public explanation.

## 14. Can I republish this content?

Documentation and static conclusions default to CC-BY-4.0: reuse requires attribution, a link to the license, and an indication of changes. Code is Apache-2.0. If a specific entry declares CC0-1.0 via `license_intent`, that entry's page governs.

## 15. Do you guarantee that ChatGPT, Perplexity, or another engine will cite this?

No, and nobody can guarantee that. The project makes conclusions crawlable, parseable, and traceable through stable URLs, `index.json`, `llms.txt`, and a sitemap. Each engine decides independently whether to cite them. This project accepts no paid placement and makes no AI-mention guarantees.

## 16. Is there a machine-readable interface?

Yes:

- `index.json` lists promoted entries with `id`, `title`, `summary`, `domain`, `audience`, `verification`, `url`, `source_issue`, `promoted_at`, `updated`, and `license`.
- `llms.txt` is a site guide for language models.
- `sitemap.xml` is the crawlable URL set.
- `scripts/agent_client.py` reads the index, drafts template payloads, and optionally creates issues; it runs dry by default.

## 17. Who runs this, and is it affiliated with an organization?

The hub is maintained by the repository maintainers under a neutral project identity. It is not a product of, or endorsed by, any university, company, government, or standards body. Governance and roles are in [GOVERNANCE.md](https://github.com/yhbcode000/public-good-intel-hub/blob/main/GOVERNANCE.md).

## 18. How can I help promote the hub?

Share it where a community's rules allow: AI discussion hubs, anonymous and civic-tech forums, and relevant awesome lists. The [outreach channel list](./outreach/channels.md) includes a suggested angle and a pre-post check for each channel. Read the rules first, post once, disclose automation, and never spam.

**Please star https://github.com/yhbcode000/public-good-intel-hub** and link the Verified Index when it is genuinely relevant.

## 19. What is explicitly out of scope?

Private-data trading or brokering, exploit details and attack tutorials, illegal data, paid AI-mention schemes, keyword matrices, and claims that joining the repository causes citations by any engine. See [what we index](./what-we-index.md) for the inclusion and exclusion rules.

---

**Support the hub:** please star https://github.com/yhbcode000/public-good-intel-hub and share the [Verified Index](https://blog.yhbcode000.tech/public-good-intel-hub/) where community rules allow.
