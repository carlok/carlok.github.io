---
title: "pacenotch is public: Claude usage limits with a vertical pace notch"
date: 2026-09-12
tags: [tool, project]
---

[pacenotch](https://github.com/carlok/pacenotch) is a new public Go
repository: a CLI, tray icon and window for macOS, Windows and Linux that
reports Claude's usage windows (5-hour session, 7-day all models, and the
7-day Sonnet/Opus windows when the plan reports them) with a thin vertical
notch drawn at the elapsed fraction of each window — the fill is past the
notch when you are ahead of an even pace, short of it when there is room left,
and the tray icon turns red on that side of the line
([d7d6da6](https://github.com/carlok/pacenotch/commit/d7d6da6),
[371aefc](https://github.com/carlok/pacenotch/commit/371aefc)). The first day
of commits also landed the usage/pace packages and terminal renderer with a
compact mode below 60 columns, parity and coverage tooling, and a CI matrix
with packaging and the README
([b8f822a](https://github.com/carlok/pacenotch/commit/b8f822a),
[b6c6151](https://github.com/carlok/pacenotch/commit/b6c6151)). The macOS
build learned to raise its window in front of other apps and to reopen it when
the running app is launched again
([9f9aa5e](https://github.com/carlok/pacenotch/commit/9f9aa5e),
[6ca1263](https://github.com/carlok/pacenotch/commit/6ca1263)). MIT-licensed
and unofficial — not affiliated with Anthropic.
