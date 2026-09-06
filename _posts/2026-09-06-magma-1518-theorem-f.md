---
title: "magma-1518-obstruction-lean: Theorem F — explicit finite models refuting 1518 ⇒ 47/614/817/3862"
date: 2026-09-06
tags: [lean4, math, research]
---

[magma-1518-obstruction-lean](https://github.com/carlok/magma-1518-obstruction-lean)
grew a third result overnight:
[Theorem F](https://github.com/carlok/magma-1518-obstruction-lean/commit/429819c)
builds an explicit parametric family of finite magmas satisfying law 1518 that
violate the four targets 47, 614, 817 and 3862 — the ETP's known 15-element
countermodels are the family's two smallest members, which then continues with
27, 39, 51, 75, … elements. A companion classification shows the
base-dependent extensions of the Z/3 shift come in exactly 8 classes for
`p ≡ 1 mod 4` and 4 for `p ≡ 3 mod 4`, with only the family and its conjugate
refuting. The 15- and 39-element members are checked by the Lean kernel via
`decide` with no axioms, and the classification rests on Gröbner bases over
`Q` and over every `F_p` with `p ≤ 257`.
