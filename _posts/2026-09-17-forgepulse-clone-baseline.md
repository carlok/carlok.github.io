---
title: "forgepulse: per-repository clone baselines, and a sidebar that folds on a 14-inch screen"
date: 2026-09-17
tags: [rust, tool]
---

The clone-trend arrows added to [forgepulse](https://github.com/carlok/forgepulse)
[two days ago](/blog/2026/09/15/forgepulse-rank-trend-arrows/) were reading
"stable" almost everywhere, and the cause was GitHub's traffic API rather than the
repositories: it reports a day's row inconsistently per repository, so at any moment
only a handful have a same-day `daily_traffic` entry while most lag behind, and a single
fleet-wide "yesterday" cutoff therefore compares most repositories against data already
included in their current total
([762ea7b](https://github.com/carlok/forgepulse/commit/762ea7b)). The fix is to compare
each repository's clone total against one day before *that repository's* own most recent
row, computed in one query through a per-repository `MAX(day)`, so the comparison never
depends on a shared calendar date — verified live, the trends now show real up and down
movement instead of universal stability.

The sidebar changed shape as well. It
[collapses into a slim first row](https://github.com/carlok/forgepulse/commit/628b103) on
narrow windows, and the breakpoint was raised to 1400px and then to 1536px
([d8cc9d8](https://github.com/carlok/forgepulse/commit/d8cc9d8),
[d859e01](https://github.com/carlok/forgepulse/commit/d859e01)) because a 14" MacBook
Pro's native 1512×982 sits above the lower cutoff even with the window maximized, which
would have kept the persistent sidebar on exactly the laptop it was meant to fold on.
