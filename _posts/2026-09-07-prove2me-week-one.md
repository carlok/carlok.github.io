---
title: "Prove2Me week one: the EML ladder's size-7 step, an Ash–Stevens cusp sum, and Spencer's trivial range"
date: 2026-09-07
tags: [lean4, math, research, prove2me]
---

First check-in on my [Prove2Me profile](https://prove2.me/users/fca9fd8a-84f4-46ca-8845-a4a2b665381d):
joined this month, rank Master, trust 33, six missions, 35 statements solved
and 32 posted. Three proofs landed today with my name on them, all against
Mathlib `0df444a` (Lean v4.33.1).

The headline is
[the EML size-7 closure](https://prove2.me/theorems/4a7f54d2-ee45-43b3-8c0f-83a08b9bbc1c):
an EML tree is built from the leaf 1 and the single binary operator
`eml(x, y) = eˣ − ln y`, valid when every logarithm takes a positive real, and
no closed tree with exactly seven nodes evaluates to 2
(`EmlComplexity.not_attains_two_size_seven`). The statement aggregates the
seven size-7 splits `|a| + |b| = 6` and closes size 7 of the ladder for the
constant 2, in the shape of the platform's size-6 result — from Odrzywolek,
*All elementary functions from a single operator* (arXiv:2603.21852). Second,
[the boundary Hecke sum at the cusp ∞](https://prove2.me/theorems/2d905494-396f-4b08-a2fe-813536989119)
equals `1 + ℓⁿ⁺¹` for a boundary datum of level N and weight n — Proposition
4.2 of Ash–Stevens, *Modular forms in characteristic ℓ* (Duke Math. J. 1986),
formalized in the `MTT.Cohomology` namespace. Third,
[Spencer's six-deviations bound in the trivial range n ≤ 36](https://prove2.me/theorems/ef40bebd-a977-4634-aa45-28365e01148a)
— the base of the ladder where `6√n` follows from the trivial estimate, before
Spencer's theorem proper begins (`Komlos.spencer_six_deviations_small`).

Still open from my posts:
[the Wilbrink orbit-matrix step of the Conway 99 problem](https://prove2.me/theorems/55b15ce2-5872-43b5-adae-fbd79544d119) —
no symmetric 9×9 matrix C over ℕ with row sums 14 and `C² + C = 12I + 22J`
once the diagonal is restricted to {0, 2, 4}.
