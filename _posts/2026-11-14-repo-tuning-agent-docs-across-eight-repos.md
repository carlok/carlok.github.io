---
title: "Eight repos get the same agent-facing hygiene: an AGENT.md, a code of conduct, coverage gates and Dependabot"
date: 2026-11-14
tags: [github, meta, project]
---

One audit, eight pull requests, all merged on 13 November: [consculpta](https://github.com/carlok/consculpta/pull/33), [cdclkit](https://github.com/carlok/cdclkit/pull/16), [caciarabot](https://github.com/carlok/caciarabot/pull/9), [roundstorm](https://github.com/carlok/roundstorm/pull/70), [guess-the-move](https://github.com/carlok/guess-the-move/pull/29), [deck-lovers](https://github.com/carlok/deck-lovers/pull/8), [fleetlens](https://github.com/carlok/fleetlens/pull/14) and [ots-explain](https://github.com/carlok/ots-explain/pull/9) now carry the same contribution surface. Each gained an `AGENT.md` — setup, the commands CI actually runs, repo layout, and three rules stated as rules: raise coverage before a commit, never commit secrets or host-specific values, keep public docs generic — plus a Contributor Covenant 2.1 code of conduct whose enforcement contact is [@carlok on GitHub](https://github.com/carlok) and no email address anywhere.

Where the gap was real, the gate came with it rather than as advice: caciarabot's CI had no coverage reporting at all and now enforces a 62 % floor on `app/caciarabot` (measured 64.50 %, 223 tests), cdclkit and deck-lovers got their own floors, and fleetlens closed at 51 tests and 90 % against an 85 % `fail_under`. caciarabot, cdclkit and ots-explain also gained issue forms, a PR template and Dependabot where none existed, and ots-explain's `SECURITY.md` lost its email fallback for GitHub private advisories.

No product code changed in any of the eight — the point was the repository, not the program: an agent arriving cold should find the same instructions in all of them, and a reviewer should see the same checklist whether the change lands in a bot, a SAT checker or a Tauri app.
