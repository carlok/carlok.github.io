---
title: "forgepulse: the 1d/7d/30d windows now count back from the newest day GitHub reported"
date: 2026-09-25
tags: [rust, tool]
---

The window columns in [forgepulse](https://github.com/carlok/forgepulse) were
mostly empty at their recent end: GitHub's traffic API lags a day or more, so
counting back from the wall clock left the newest days without rows and the 1d
column read zero for nearly every repository
([7f5acb4](https://github.com/carlok/forgepulse/commit/7f5acb4)). The windows now
count back from the newest day that at least half of all repositories have a row
for, and each window is capped at that day, so a stray early same-day row cannot
leak in as a partial day or move the anchor — a plain `MAX(day)` would let one
early reporter blank out everyone else. It also makes 1d genuinely one day: the
old `>= now − 1 day` spanned up to two. It is the same lag the [per-repository
clone baselines](/blog/2026/09/17/forgepulse-clone-baseline/) were added for, now
fixed at the window itself rather than at the comparison.
