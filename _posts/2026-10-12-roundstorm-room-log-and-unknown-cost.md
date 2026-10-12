---
title: "roundstorm: a room's log dies with the room, and unknown cost stays unknown"
date: 2026-10-12
tags: [tool]
---

[roundstorm](https://github.com/carlok/roundstorm) closed five issues in a day
of follow-up work on the local-first deliberation app. The events table was
never pruned, so a cleared or deleted room's turns outlived it — the log is a
debugging aid, not an audit trail past the room's life, so a delete now takes it
with it, a decision written down in `db.ts` and `docs/design.md` rather than left
implicit ([#43](https://github.com/carlok/roundstorm/pull/43)). Cost had the
opposite problem: only the Claude adapter reports one, other brains stored
`NULL`, and the persona lab and the headless output summed that as 0, so a
comparison between a priced and an unpriced arm read as a saving; cost is now a
null-aware sum with a priced-turn count, rendered `n/a` or "at least" when only
part of the total is known ([#44](https://github.com/carlok/roundstorm/pull/44)).

The rest is hardening. A test drives the CLI's `SIGINT` handling against a
fixture brain that starts a real child process and hangs, asserting exit 130,
that no deliberation is left running or stopping in the store, and that the
brain process is gone — checked by mutation, since removing either
`abortAllDeliberations` or `terminateAll` from the handler makes it fail
([#45](https://github.com/carlok/roundstorm/pull/45)). Housekeeping collapsed
three copies of `LEVEL_LABEL` and four spellings of the `__result__:` transcript
sentinel into one of each, and `PATCH /rooms/:id` with the stop, interrupt and
extend routes now answer 404 for an unknown id instead of an empty 200
([#46](https://github.com/carlok/roundstorm/pull/46)); CI runs the suite under
coverage and publishes the table in the job summary, informational only, with
`shell: bash` so a failing suite still fails the job
([#47](https://github.com/carlok/roundstorm/pull/47)).
