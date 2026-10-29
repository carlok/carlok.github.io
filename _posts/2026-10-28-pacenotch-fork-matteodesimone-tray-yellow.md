---
title: "carlok/pacenotch was forked by matteodesimone, and his tray-icon patch shipped as v0.2.2 the same day"
date: 2026-10-28
tags: [tool, github]
---

[carlok/pacenotch](https://github.com/carlok/pacenotch) was forked by
[matteodesimone](https://github.com/matteodesimone/pacenotch) on 28 October —
Matteo De Simone, in Italy, who [forked LeanFrontier](https://github.com/matteodesimone/LeanFrontier)
in August and used it the way the corpus expects, as a branch to submit from.
This time the fork came back as a patch to a different project: [PR #1](https://github.com/carlok/pacenotch/pull/1)
noticed that in macOS light mode the menu-bar icon uses `LightBars()`, whose
on-pace fill `0xB25000` is an amber chosen to stay readable as text on white —
at menu-bar size almost the same as the ahead red, while the window shows
yellow for the same row. `TrayBars(dark)` keeps the palettes but gives the
light tray `0xFFCC00`, Apple's system yellow, since an icon carries no text;
the window palette is untouched, and a new test pins the tray's on-pace fill to
yellow in both modes.

Merged as [368ad6a](https://github.com/carlok/pacenotch/commit/368ad6a) and
released by CI as [v0.2.2](https://github.com/carlok/pacenotch/releases/tag/v0.2.2),
where GitHub records it as the repository's first outside contribution.
