---
title: "pacenotch: an Ultra account has no 5-hour window, so the app says that instead of drawing an empty bar"
date: 2026-11-01
tags: [tool]
---

Verified Ultra accounts — the plan that used to be Max 20x — have no five-hour limit, so the usage endpoint returns no `five_hour` window. [pacenotch](https://github.com/carlok/pacenotch) handled that badly: the window showed nothing and the tray icon drew a hollow top bar that reads as *idle* rather than *not applicable* ([0344c63](https://github.com/carlok/pacenotch/commit/0344c63), [#4](https://github.com/carlok/pacenotch/pull/4)).

The fix adds a `View.NoSession` state — windows exist, none of them is `five_hour` — and each surface says it in its own register: a dim "no 5-hour limit reported (Ultra plans have none)" line in the window, a `5h none` row in the compact layout, and a tray icon holding only the 7-day bar, centred, when that one exists. The GUI's no-windows text now names Ultra, while the CLI text is deliberately untouched so the reference-script parity test keeps passing, and no 5-hour bar is ever invented out of the 7-day numbers.

Two fixtures carry it — `ultra-seven-day-only` and `ultra-five-hour-null`, with golden output, screenshots and a README note — over `make test`, `make test-gui` and `go vet -tags gui` at 100% GUI coverage and 99.8% on the module. The honest limit is in the pull request: nobody has seen a real Ultra endpoint response, so the code treats `five_hour` as missing when it is absent *or* null, which is what `Parse` already dropped.
