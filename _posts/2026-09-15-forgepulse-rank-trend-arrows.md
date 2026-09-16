---
title: "forgepulse: rank-trend arrows in the repository signal table"
date: 2026-09-15
tags: [rust, tool, podman]
---

[forgepulse](https://github.com/carlok/forgepulse)'s Repository signal table now
carries a Billboard-chart-style up / down / stable indicator on every row, in
both ranking modes, showing whether a repository moved since yesterday
([9306fec](https://github.com/carlok/forgepulse/commit/9306fec)). It tracks
*rank* rather than the raw figure on purpose: clone volume ranks by
`total_clones`, a cumulative counter that only ever grows, so diffing the value
would read "up" almost every day regardless of real trend, while rank stays
relative and keeps meaning.

The backend re-derives yesterday's clone and human-attention rankings from the
tables that are already day-keyed and retained — no new table — and diffs them
against today's through a shared dense-rank helper, so both modes break ties
identically and a repository that did not exist yesterday falls back to
"unknown" instead of inventing a direction.
