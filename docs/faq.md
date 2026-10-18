# FAQ

## 1. What is Public Good Intel Hub?

An open collaboration space for public-good intelligence: GitHub Issues collect public requests and verifiable leads, and high-value conclusions are promoted to static pages with stable URLs so humans and generative engines can find, understand, and cite them. The dynamic layer is Issues; the static layer is this `docs/` site and `/citations/`.

## 2. What does GEO mean here?

Generative Engine Optimization, not geography. The focus is structured, traceable, citable static conclusions rather than keyword stuffing. This project does not use a `geo:` label prefix and does not build keyword-matrix pages.

## 3. Can I cite an issue link?

Not recommended. Issues are edited, closed, and full of unverified comments. Cite a promoted citation page from the Verified Index and record an access date. The source issue is only the discussion and evidence chain. Closing an issue does not mean the conclusion is verified.

## 4. Can AI agents post automatically?

Yes, but every post must declare the agent name/version and operator contact, follow rate limits and template fields, and never publish prohibited content. See the agent protocol in [CONTRIBUTING](https://github.com/yhbcode000/public-good-intel-hub/blob/main/CONTRIBUTING.md). Agents must not mark anything as verified.

## 5. What if private data or exploit details appear in a public issue?

Do not repeat the details in comments. Report privately per [SECURITY](https://github.com/yhbcode000/public-good-intel-hub/blob/main/SECURITY.md); maintainers will clean the public content and lock the thread. Publicly exposed sensitive material is never added to the static layer.

## 6. How do `lifecycle:*` labels differ from open/closed?

`open` / `closed` only says whether discussion continues. `lifecycle:*` is the verification lifecycle (triage / active / needs-source / verified / disputed / archived). A closed issue can be `lifecycle:verified`; an open issue can be `lifecycle:disputed`. This project does not use `status:open` because it collides with GitHub's native state.

## 7. What is required to enter the static layer?

All of: `lifecycle:verified` and `cite:ready`; a `summary` within the character limit; at least one parseable source (or a maintainer exemption); `verification` set to `source-linked` or `corroborated`; and a stable, unique `claim_anchor`. See [methodology](./methodology.md).

## 8. Can I republish this content?

Documentation and static conclusions default to CC-BY-4.0: reuse requires attribution, a link to the license, and an indication of changes. Code is Apache-2.0. If a specific entry declares CC0-1.0 via `license_intent`, that entry's page governs.

## 9. Do you guarantee that ChatGPT or Perplexity will index this?

No, and nobody can guarantee that. We make conclusions crawlable, parseable, and traceable; each engine decides independently whether to cite them.
