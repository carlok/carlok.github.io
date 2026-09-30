---
title: "diaz-modulus-lean and prove2me-logs: note 1.11 on rational squared moduli, and the fifth size wave"
date: 2026-09-30
tags: [lean4, math, research]
---

The Diaz companion note reached
[v1.11](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.11)
with three corollaries on rational squared moduli, each machine-checked: if
`t^2 + pi^2` is rational for a real `t != 0` with `e^t` algebraic, then
`e^(i*gamma/pi)` is transcendental for every rational `gamma != 0`
(Corollary 3.8), so the two remaining open statements cannot both fail at
rational data; logarithms of algebraic numbers that are algebraic over `Q(pi)`
with rational squared moduli are rational multiples of one another up to
conjugation (Corollary 6.9); and at most one pair `±t` makes `t^2 + pi^2`
rational, so `(log 2)^2 + pi^2` and `(log 3)^2 + pi^2` are not both rational
(Corollary 6.10). Section 4 adds a specialisation of Waldschmidt's 1973 theorem,
checked with that theorem as a hypothesis. The mirrored library stands at 268
results: the [fifth size wave](https://github.com/carlok/diaz-modulus-lean/commit/4f6ffd5)
adds six second proofs and one node, closing at 268 of 268, and
[prove2me-logs](https://github.com/carlok/prove2me-logs) carries the same day
from the research side
([9bed59e](https://github.com/carlok/prove2me-logs/commit/9bed59e),
[1c5714c](https://github.com/carlok/prove2me-logs/commit/1c5714c)).
