---
title: "red-ink sprint 29: a training room with a dummy and a move-cost strip, medals with edges, and a limiter the mix actually needed"
date: 2026-11-06
tags: [games]
---

[red-ink](https://github.com/carlok/red-ink) built ten backlog items in sprint 29 and moved the regression from 61 tests to 70. The new training room puts a dummy in front of a strip of move costs — jab 10, heavy 24, dodge 16 — that strikes out what the stamina on hand cannot afford, with a guard switch on a button and T; a test drives 240 frames of heavies and requires the dummy never to attack, move or die ([#26](https://github.com/carlok/red-ink/pull/26)). Medals got real edges — Untouched, Sharp at 85 percent, Quick at 26 / 31 / 40 / 46 / 38 / 39 seconds, no medal from Practice or the second pass, save version 3 — and the alert mark that warns of an incoming blow got a dark rim after measurement found it at 1.6 to 1 against bout 4's pale floor, which the rim moved to 2.6 ([f238b34](https://github.com/carlok/red-ink/commit/f238b34)).

Two items came back with numbers rather than opinions. A new test times the work instead of the frame rate: the simulated tick runs at 0.0025 to 0.0026 ms against a 16.7 ms frame with a 0.1 ms ceiling, and the JavaScript side of `scene.render` at 1.21 to 1.38 ms against a ceiling of 8. The mix needed a limiter after all — eight runs of the loudest scene peaked from −4.4 to −0.4 dBFS, so a compressor now sits on the output with its fixed +1.71 dB makeup gain measured offline and trimmed, taking the same scene to −2.4 dBFS worst case while an offline 2.0 tone comes out at 0.763.

CI got the same treatment: Lighthouse and axe moved to `tools/qa` with their own lockfile, cutting the regression's install from 346 MB and 252 packages to 114 MB and 30, `lib/babylon.js` is now checked against a rebuild, and Chrome for Testing is pinned at 156.0.8078.80 — which failed its first runner run in 20 s until `withPage` added `--no-sandbox`, since Chrome for Testing cannot make its sandbox under the runner's user-namespace limits ([5234d4a](https://github.com/carlok/red-ink/commit/5234d4a), [5b03adb](https://github.com/carlok/red-ink/commit/5b03adb)).
