---
title: "forgepulse: the rank column stops stretching to the row height"
date: 2026-09-17
tags: [rust, tool]
---

The [rank-trend arrows](/blog/2026/09/15/forgepulse-rank-trend-arrows/) in
[forgepulse](https://github.com/carlok/forgepulse)'s Repository signal table
[cost every row its bottom border alignment](https://github.com/carlok/forgepulse/commit/6544467):
`display: flex` on `.rank-share`, added to stack the arrow, pulled that `<td>`
out of table layout, so it stopped growing to the row's real height and stayed
clipped to its own content while the Name column stretched normally for longer
descriptions. Dropping the flex display and keeping the existing block-span
stacking restores the alignment — two lines of CSS, which is what a change made
to fit a two-character indicator should have cost in the first place.
