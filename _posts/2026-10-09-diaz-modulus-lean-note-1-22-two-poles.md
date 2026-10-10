---
title: "diaz-modulus-lean: note v1.22, two poles, and Kirby's weak Schanuel conjecture at a candidate"
date: 2026-10-09
tags: [lean4, math, research]
---

The Diaz companion note is now at
[v1.22](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.22):
[diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean) ports the seven
nodes published on Prove2Me on 9 October and the mirrored library stands at all
389 proved results on Lean's three standard axioms
([3450aec](https://github.com/carlok/diaz-modulus-lean/commit/3450aec)). For
`u ∉ ℚ̄` with `uū` algebraic and distinct non-zero algebraic `a₁, a₂`, the space
`H₀ + ℚ̄·u/(u²−a₁) + ℚ̄·u/(u²−a₂)` carries a rank-one 2×3 configuration — the
progression `b, bu², bu⁴, bu⁶` — that no four-dimensional `H₀ + ℚ̄w` inside it
carries, with no conjugation condition; at a candidate, under Roy's theorem, the
two terms are not both in `ℒ̃`, and in the family `aᵢāᵢ = |u|⁴` their sum is not
(substitutions in Diaz 2007, Théorème 7(2) = Fischler 2001, Lemma 6.1, not
claimed). Under the case `n = 2` of Kirby's weak Schanuel conjecture every
candidate has `Im u ∈ πℚ`, so Diaz's conjecture is equivalent to the single
relation `t² + π²` transcendental for real `t ≠ 0` with `eᵗ` algebraic — the
remark is now formal rather than prose. Chapter 13 of the blueprint gained the
three results from the manuscript, the pair dichotomy, two candidates on an
axis-parallel line and mixed rigidity, with the four nodes their proofs import
([68a87a7](https://github.com/carlok/diaz-modulus-lean/commit/68a87a7)). The same
day's [prove2me-logs](https://github.com/carlok/prove2me-logs/commit/a1c2390)
entry carries the mission from the research side.
