---
title: "curve-symmetry-lean closes R01: the quartic's genus three, from an explicit basis of differentials"
date: 2026-09-29
tags: [lean4, math]
---

Roadmap item R01 in [curve-symmetry-lean](https://github.com/carlok/curve-symmetry-lean)
is closed: the quartic `Re(z⁴) = 1` is now proved to have genus three, and the
proof reaches it from an explicit basis of holomorphic differentials rather than
from Riemann–Hurwitz. Three steps, each a clean `check.sh` run against
`mathlib-v4.34.0-reuse`: first the chart at infinity for `y⁴ = 2 − x⁴`, where
`f = 2 − x⁴` and `g = 2s⁴ − 1` are squarefree of degree four so R01c-2 applies to
both Kummer fields, and `F·dx` is regular at the place pulled back from `(0, ζ)`
with `ζ⁴ = −1` exactly when `φ(F)/s²` lies in the local ring
([fdc7192](https://github.com/carlok/curve-symmetry-lean/commit/fdc7192)); then the
isotypic split of the holomorphic differentials under `y ↦ i·y`, which recovers
each `aⱼ(x)·yʲ·dx/y³` from `F`, `σF`, `σ²F`, `σ³F` with coefficients `±1, ±i`
([2024297](https://github.com/carlok/curve-symmetry-lean/commit/2024297)); then the
degree bound `deg aⱼ + j <= 1` at infinity, leaving `dx/y³`, `x·dx/y³` and `dx/y²`
to span the holomorphic space and forcing genus three
([b8c207e](https://github.com/carlok/curve-symmetry-lean/commit/b8c207e)). The same
commit settles Remark 5 of the note as printed — `Re(z⁴) = 1` has four rotations
and genus three, every curve of the `m = 2` family has genus two, and no direct or
opposite similarity carries the quartic onto one of them — and the axiom audit
climbed 1,991 → 2,034 → 2,058 across the three steps. The note and its Lean port
went public in the same week, with the launch described
[here](/blog/2026/09/30/curve-symmetry-lean-public/).
