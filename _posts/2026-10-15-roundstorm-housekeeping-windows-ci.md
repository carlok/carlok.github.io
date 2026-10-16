---
title: "roundstorm: a failed request stops being silent, and an informational Windows cell"
date: 2026-10-15
tags: [tool, security]
---

Two follow-ups landed in [roundstorm](https://github.com/carlok/roundstorm) behind [0.1.1](/blog/2026/10/15/roundstorm-0-1-1/). Six raw `fetch(apiUrl(...))` calls in `App.tsx` now go through `api()` with a `call` helper, and the behaviour change that comes with it is the point: rename, duplicate and agent delete used to ignore a failed response silently, and now show the server's error and stop ([#59](https://github.com/carlok/roundstorm/pull/59), [9ae96b1](https://github.com/carlok/roundstorm/commit/9ae96b1)). The same pull request writes down the event convention `logEvent` had been following by hand — room, deliberation and agent ids are columns, other entities' ids belong in the payload — moves the two events that concerned a room but carried no `roomId` (`deliberation.interrupted`, `round.restarted`) onto it so they appear in the room's log, and gives `backup.created` one shape, `{ via, path, bytes }` with `path` null for a download, on both routes, with a test.

[#60](https://github.com/carlok/roundstorm/pull/60) adds an informational `windows-latest` cell to CI: typecheck and `npm test` run there with `continue-on-error`, the `sh`-driven tests skip on win32, and nothing can be blocked by the third platform the app also ships for ([a77f319](https://github.com/carlok/roundstorm/commit/a77f319)). It is the CI half of [issue #37](https://github.com/carlok/roundstorm/issues/37).
