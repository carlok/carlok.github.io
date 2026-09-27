---
title: "LeanFrontier: a Markov slope-scale gcd identity from the outside contributor"
date: 2026-09-27
tags: [lean4, math, project]
---

[LeanFrontier](https://github.com/carlok/LeanFrontier) merged
[#385](https://github.com/carlok/LeanFrontier/pull/385), a 160-line
[`LeanFrontier/NumberTheory/MarkovEquation/SlopeScaleGCD.lean`](https://github.com/carlok/LeanFrontier/blob/main/LeanFrontier/NumberTheory/MarkovEquation/SlopeScaleGCD.lean)
carrying three new declarations, submitted through the fork of
[qazW12345](https://github.com/qazW12345) — the outside contributor whose fork
was [the intake route](/blog/2026/09/12/leanfrontier-fork-qazw12345/) for the
Nesbitt submission, and whose resolution of the corpus's only conjecture
[closed Field Note 16](/blog/2026/09/26/leanfrontier-field-note-16/) the day
before.

The identity itself: for primitive integers `x, y` and odd `M`, the quadratic
pair `L = x² + y² + 3Mxy`, `T = y² − x²` and the linear pair `U = 3Mx + 2y`,
`V = 3My + 2x` have exactly the same integer common divisors, so
`gcd(L, T) = gcd(U, V)`; after dividing out a common divisor, the elementary
relations `L + T = y·U` and `L − T = x·V` reconstruct the primitive quotient
factors as gcds. It is elementary integer arithmetic — it assumes neither the
Markov equation nor the Markov uniqueness conjecture the corpus adopted as its
new open question — and it is useful for the same reason it was found:
a gcd introduced in a slope-scale reduction of Markov collision arithmetic can
be read off the linear pair instead.

The submission is machine-derived and honest about it — GPT-5.6 Sol / ChatGPT
found the identity while exploring that arithmetic and formalized it at the
human operator's request, with no claim of publication-level novelty — and the
trusted receiver admitted it on the ordinary route: kernel recheck pass, no
exact Mathlib fingerprint match, three new declarations and 5,849 bytes of
Lean source. The corpus's own record is at
[carlok.github.io/LeanFrontier/notes](https://carlok.github.io/LeanFrontier/notes/).
