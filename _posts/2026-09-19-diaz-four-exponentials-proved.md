---
title: "diaz-modulus-lean and prove2me-logs: the four exponentials theorem in transcendence degree one is proved"
date: 2026-09-19
tags: [lean4, math, research]
---

The 1973 construction whose four children
[began to close](/blog/2026/09/17/diaz-1973-children-close/) in
[diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean) is finished, and
with it the four exponentials theorem in transcendence degree one. The norm child
went first: `FourExp.norm_to_polynomial_alg` is proved
([a38d9db](https://github.com/carlok/diaz-modulus-lean/commit/a38d9db)) by linear
algebra rather than the paper's conjugates — the value is presented as
`Π ∈ ℤ[X][Y]` reduced modulo the monic `Q`, `P = det M` is the determinant of
multiplication by `Π` in the basis `1, Y, …, Y^(d−1)`, non-vanishing comes from a
kernel vector that would contradict the minimality of `Q`, and smallness from the
adjugate identity `M·adj M = (det M)I`. That made the core,
`FourExp.construction_core_1973`, a Proved node by cascade.

Three small leaves then closed the construction — rank-one parametrization, the
growth of the majorants `x²√log x` and `x²/√log x`, and the counting inequality
(`80N⁴/√log N` unknowns against `98N⁴/√log N` equations) — each accepted on its
first submission, and the cascade proved `FourExp.auxiliary_construction`,
`FourExp.small_polynomials_of_counterexample`,
`DiazModulus.four_exponentials_trdeg_one` and the period-aligned half of the Diaz
branch that reduces to it ([4118fcc](https://github.com/carlok/diaz-modulus-lean/commit/4118fcc)):
if `x₁, x₂` and `y₁, y₂` are ℚ-linearly independent pairs whose four products have
algebraic exponentials, the field they generate has transcendence degree at least
two — every step, from Siegel's lemma to the final contradiction, checked by Lean,
and the [mirror now holds 154 of 154 entries](https://github.com/carlok/diaz-modulus-lean/commit/cc852b7).
The journal in [prove2me-logs](https://github.com/carlok/prove2me-logs) records the
same two steps with the nodes and submissions
([51e8586](https://github.com/carlok/prove2me-logs/commit/51e8586),
[8a676e5](https://github.com/carlok/prove2me-logs/commit/8a676e5)).
