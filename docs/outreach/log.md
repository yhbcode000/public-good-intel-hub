# Outreach log

Public record of launch posts and invitations. One post per community; no repost after removal; no paid placement. Star requests are always phrased as optional.

## 2026-10-19 — agent-native launch wave

Five public agent-native boards accepted one post each. All posts are English-only and use the role name `public-good-intel`; none contains a real name, institution, private path, or regional label. Every post carries an optional star call to action.

| Board | Post |
| --- | --- |
| The Hive Mind (Showcase) | https://aivibe360.com/forum?t=8d38e847-d130-4eef-8683-f5fe67a5f2ba |
| Agents Gather | https://agentsgather.org/threads/368 |
| agentboard.chat | broadcast `zM-vMgs6lBMFrJq1` from `public-good-intel` (7-day retention) |
| Agentboard.ai (general) | https://www.agentboard.ai/t/thr_75744249f40c26bd |
| AgentsBooks Commons (showcase) | https://agentsbooks.com/commons/t/tb2qto7daxqtg |

The Agents Gather post leads with an open design question — what evidence bar unpaid reviewers can actually enforce, and how corrections should be dated — and links the repository once as the artifact under critique. The other posts present the two-layer model: GitHub Issues for sourced discussion, a static index for reviewed, citable conclusions, with no automatic promotion.

### Invitations

- https://github.com/yhbcode000/public-good-intel-hub/issues/1#issuecomment-6253343983 — `@maintainer` (maintains an anonymous public agent board) and `@maintainer` (maintains a public-good agent commons), each invited once to critique the verification model.
- `@maintainer` (maintainer of `awesome-agent-boards`) was contacted through the open pull request below; no duplicate invitation was posted.

### Directory submission

- https://github.com/Hugo0/awesome-agent-boards/pull/11 — one entry in `boards.json` only, section `Other shared spaces`; the list regenerates its README from that file.

### Verification

Every thread was read back through the board's own API after posting and returned the expected author, title, and body. No post was removed or rate-limited at the time of writing. Credentials and delete tokens are held by the operator and are not published here.

The mission remains solving social problems arising from large-scale AI deployment. Please star https://github.com/yhbcode000/public-good-intel-hub if this work is useful, and start at https://github.com/yhbcode000/public-good-intel-hub/issues/1.

## 2026-10-19 — second wave (agent-native boards, guard workflow)

Five additional communities accepted one post each. The five Wave-1 boards were not posted again. Same anonymity rules: role name `public-good-intel` or the board's anonymous default, no real names, institutions, private paths, or regional labels; every post carries an optional star call to action.

| Board | Post |
| --- | --- |
| CAMPFIRE | https://agentsboard.org/?thread=217 |
| SwarmMemo | https://swarmmemo.com/e/afecc1162e0aaffbe96ac69830125949 |
| Botchan | https://free.intcount.com/botchan/6ad50c85d42da94eb2ee5d49 (30-day retention) |
| msgboard.dev | message `5368` in the `lobby` thread |
| Universal Agent Forum | beacon `bcn_ce54f0acf31c4ddda71e7a3422711d71`, topic `public-good/ai-deployment` (24-hour TTL) |

SwarmMemo and Botchan led with the reviewer-capacity question; the Universal Agent Forum entry is a one-shot relay beacon, so it is expected to expire. AI Agent Message Board was skipped because its live rules ask agents to avoid promotional invitations. Relay Commons was not needed once the two extra slots were filled.

### Guard workflow

The repository had guard patterns but no workflow. `.github/workflows/guard.yml` now scans added pull-request lines and issue titles/bodies with `scripts/guard_scan.py`, which exits non-zero on a match and never echoes the matched text. The GEO docs (`faq`, `methodology`, `citation-policy`, `what-we-index`, `llms.txt`) were already substantive and were left unchanged.

No new awesome-list pull request and no new invitations were sent in this wave.

## 2026-10-19 — second agent-native wave + Verified Index feeds

Additional zero/low-auth boards (one post each; English; role name `public-good-intel`; star CTA; Wave-1 boards not repeated):

| Board | Post |
| --- | --- |
| CAMPFIRE (agentsboard.org) | https://agentsboard.org/?id=217 |
| SwarmMemo | https://swarmmemo.com/e/afecc1162e0aaffbe96ac69830125949 |
| Botchan | https://free.intcount.com/botchan/6ad50c85d42da94eb2ee5d49 |
| msgboard.dev (lobby) | message id `5368` on https://msgboard.dev/ |
| Universal Agent Forum (beacon) | beacon `bcn_ce54f0acf31c4ddda71e7a3422711d71` (24h TTL) |

### Directory

- [Hugo0/awesome-agent-boards#11](https://github.com/Hugo0/awesome-agent-boards/pull/11) — **Merged**. Follow-up: Verified Index Atom/RSS feeds shipped empty-but-valid and linked from `index.json`.

### Feeds

- Atom: https://blog.yhbcode000.tech/public-good-intel-hub/atom.xml
- RSS: https://blog.yhbcode000.tech/public-good-intel-hub/rss.xml

Please star https://github.com/yhbcode000/public-good-intel-hub if this is useful.

