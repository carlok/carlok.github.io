---
title: "diaz-modulus-lean: notes 1.13 to 1.15 — Roy's strong six exponentials, and the route that stops at u³"
date: 2026-10-02
tags: [lean4, math, research]
---

Three more companion-note versions landed on 1 October, taking the mirrored
library from 283 to 307 results. The
[companion note reached v1.13](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.13)
(293 results) with the consequences of Roy's strong six exponentials theorem
that are now machine-checked — Diaz's Corollaires 1, 2, 4 and 5 of the 2007
paper in general, and at a candidate the facts that `u³` and axis multiples
leave `ℒ̃`, so `e^(βπu)` is transcendental
([f3c56f5](https://github.com/carlok/diaz-modulus-lean/commit/f3c56f5)).
[v1.14](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.14)
(304) then takes all of Section 2 of Diaz 2007 under the same hypothesis, and
pins down where that route stops: a strong six exponentials configuration fed
with a candidate's own data exists only for `k = 2` and `3`, so the theorem
excludes `u²` and `u³` from `ℒ̃` and no higher power
([2c75c4b](https://github.com/carlok/diaz-modulus-lean/commit/2c75c4b)).
The day closes at
[v1.15](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.15)
(307), where the strong four exponentials conjecture plus Baker's theorem
implies the sharp four and that implies Waldschmidt's strong five, and
Waldschmidt's 1988 remark is corrected to compare the strong five with the
sharp four rather than with Conjecture 1.2
([631d51f](https://github.com/carlok/diaz-modulus-lean/commit/631d51f)). No new
mathematics is claimed, and
[prove2me-logs](https://github.com/carlok/prove2me-logs) carries the same day
from the research side, down to a note that Brownawell 1974 is "related by the
exponential function"
([d89c37f](https://github.com/carlok/prove2me-logs/commit/d89c37f)).
