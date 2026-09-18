---
title: "diaz-modulus-lean and prove2me-logs: the 1973 construction's four children start closing"
date: 2026-09-17
tags: [lean4, math, research]
---

The restated 1973 construction
[split in four](/blog/2026/09/16/diaz-1973-construction-split/) the day before has
begun to close in [diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean),
one archive-and-port step per child. The field came first: `FourExp.trdeg_one_presentation`
makes `ω = x₁y₁` transcendental by Hermite–Lindemann, everything else algebraic over
`Q(ω)` from transcendence degree one, then a primitive element scaled to an integral
generator with a monic minimal relation and a common denominator for the eight numbers
([5f3ee4e](https://github.com/carlok/diaz-modulus-lean/commit/5f3ee4e)). Two of the
remaining children needed restating first, because `auxiliary_function` and
`norm_to_polynomial` had omitted that the four exponentials are algebraic — without it
the `ω`-degree of the powers `(e^{x_i y_2})^{jb}` is unbounded — so they came back as
`auxiliary_function_alg` and `norm_to_polynomial_alg` with the old pair left as a dead
branch ([fced437](https://github.com/carlok/diaz-modulus-lean/commit/fced437)).

The auxiliary function then followed: split into the integer linear system whose
solutions make it vanish on the grid — derivatives as a coefficient recursion over
`Z[X][Y]`, powers of the algebraic `e^{x_i y_j}` reduced through integer annihilators,
reduction modulo the monic `Q`, and a majorant calculus for degrees and heights
([71ebcba](https://github.com/carlok/diaz-modulus-lean/commit/71ebcba)) — and Siegel's
lemma over `Z` with an entrywise bound and non-vanishing from the minimality of `Q` at
exponent `κ₁ + 2` ([3b78323](https://github.com/carlok/diaz-modulus-lean/commit/3b78323)),
which turned `auxiliary_function_alg` Proved by cascade. Extrapolation closed next,
Waldschmidt 1973 Lemma 5 from the Cauchy estimate with zeros already ported: `t₁·t₂`
grid points of order at least `S`, radius `R = (ρ+1)N` so the contraction ratio is at
most `1/(N−1)`, and explicit asymptotics giving `exp(−N⁴√log N / 32)`
([f73d21f](https://github.com/carlok/diaz-modulus-lean/commit/f73d21f)). Only the norm
child is still open, and the mirror now carries
[154 of 154 entries](https://github.com/carlok/diaz-modulus-lean/commit/cc852b7).

The journal entries in [prove2me-logs](https://github.com/carlok/prove2me-logs) carry
the same three steps — the field with the hypothesis that had been missing, the
existence of the auxiliary function, and the extrapolation
([30ddc9c](https://github.com/carlok/prove2me-logs/commit/30ddc9c),
[0675986](https://github.com/carlok/prove2me-logs/commit/0675986),
[b74d05a](https://github.com/carlok/prove2me-logs/commit/b74d05a)) — stating what each
closed node was, and what remains unproved.
