---
title: "sharp-symmetry-bounds-lean is public: sharp symmetry bounds for real plane curves"
date: 2026-09-17
tags: [lean4, math, project]
---

[sharp-symmetry-bounds-lean](https://github.com/carlok/sharp-symmetry-bounds-lean)
is a new public Lean 4 repository formalizing
[Theorem 1 of the working note "Sharp symmetry bounds for real algebraic curves"](https://github.com/carlok/sharp-symmetry-bounds-lean/commit/4408003):
if an infinite real plane curve of degree `d ≥ 2` is irreducible over the complex
numbers and is not a circle, its Euclidean symmetry group is finite — the
orientation-preserving part cyclic of order at most `max(d, 2d − 4)` and the full
group of order at most `2d` — both bounds are attained in every degree, and for
`d ≥ 5` the curves attaining the rotation bound are classified, up to
orientation-preserving similarity, as `Re(z^(d−2)(|z|² + a)) = 0` with `|a| = 1`
and `a` not real.

`Challenge.lean` states the theorem on Mathlib imports alone and `Solution.lean`
proves it from the modules under `lean/`, with `comparator.json` and
`formalization.yaml` carrying the Palomar entry configuration and metadata in the
layout the magma-1518 package already uses. The repository is extracted from a
larger private development down to the modules Theorem 1 needs, is Apache-2.0,
and its proofs close over only `propext`, `Classical.choice` and `Quot.sound`.
