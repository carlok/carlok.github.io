---
title: "forgepulse: an award badge for repositories in the top 10 of both rankings"
date: 2026-10-03
tags: [rust, tool]
---

[forgepulse](https://github.com/carlok/forgepulse) publishes two rankings of the
same fleet — human attention, built from unique views, external referrers and
new stars and forks, and raw clone volume — and they rarely agree, so a
repository that reaches the top ten of *both* now carries an award badge beside
its rank, in either view
([55028f2](https://github.com/carlok/forgepulse/commit/55028f2)). The condition
lives in `web/src/lib/rank.ts` as `inBothTopN`, which is true only when the
attention rank exists and both ranks are 10 or better; the badge is styled in
`styles.css` and the rule is covered by `rank.test.ts`.
