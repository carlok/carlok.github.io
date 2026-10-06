---
title: "roundstorm: the test suite stops opening the real database and running real brains"
date: 2026-10-06
tags: [tool]
---

A Dependabot pull request that failed one Ubuntu cell with "database is locked" was not the bump's fault. Importing nearly anything under `server/src` imports `db.ts`, which opens a SQLite file at import, and ten test files never set `ROUNDSTORM_DATA` first — so they opened the default data directory, the real database on a developer's machine, and on CI one file shared by every parallel test process racing to create and migrate it ([44a5bd9](https://github.com/carlok/roundstorm/commit/44a5bd9)). A second bug surfaced in the same empty-`HOME` experiment: `gate.test.ts` called `/api/bootstrap`, which probes every brain, so `npm test` executed the real `agy` and `cursor-agent` CLIs on any machine that had them. `scripts/test-setup.mjs` is now preloaded into every test process and hands each its own empty data directory rather than relying on the next author to remember, `gate.test.ts` hits `/api/memory` instead, and a re-run under an empty `HOME` passes 196 of 196 while creating nothing there.
