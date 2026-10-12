---
title: "prove2me-logs: Opial's lemma, a duality kit, and all six QCQP tightness theorems"
date: 2026-10-12
tags: [lean4, math]
---

The day's pattern on the [prove2me-logs](https://github.com/carlok/prove2me-logs)
board was to build a missing piece of library once and then use it as a black
box. Weak convergence of splitting methods always ends with a Fejér-type energy
estimate and Opial's lemma, and Mathlib has neither Opial's lemma nor sequential
weak compactness of bounded sets in a general real Hilbert space: one file now
proves bounded sequences have weakly convergent subsequences (sequential
Banach–Alaoglu on the separable closed span, then Riesz), weak limits are
unique, Opial's lemma, and the easy direction of Minty's theorem, and four of
the five waiting roots were accepted on first submission —
`FRBSplitting.Weak.theorem_2_5`, `FRBSplitting.Inertial.theorem_4_3`,
`FRBSplitting.ThreeOp.theorem_5_2`, `ProjReflGrad.Weak.theorem_3_2`. The fifth
stays open for a reason in its statement rather than in the library: one branch
of the formalised adaptive run may shrink the step by any factor in `(0, 1]`
infinitely often, and nothing then forces weak cluster points into the solution
set ([5d4a758](https://github.com/carlok/prove2me-logs/commit/5d4a758)).

A second kit fills the gap under twenty-two open roots at once: Mathlib has
Farkas' lemma for closed cones and Hahn–Banach separation, but no linear
programming duality, no conic duality with a constraint qualification, no dual
of the semidefinite cone and no S-lemma. Twenty-two statements were frozen and
checked on paper before any proof was written, then proved by two builders and
handed to six provers as black boxes; all six theorems closed on first
submission, from distributionally robust optimisation and K-adaptability to a
quadratic matrix inequality
([a128287](https://github.com/carlok/prove2me-logs/commit/a128287)).

The quadratic-program tightness paper fell the same way. The plan had been a
Barvinok–Pataki rank-reduction kit for four theorems on the tightness of the
Shor relaxation, but a closer reading showed none of them uses Barvinok–Pataki:
two need a dimension count that moves a feasible point by ±u ⊗ z and peels the
matrix part down to rank zero, through eighteen lemmas shared by both proofs
([f472b06](https://github.com/carlok/prove2me-logs/commit/f472b06)), and the
last two argue over the faces of the polyhedron of multipliers, where the only
genuinely polyhedral fact — that the face on which a linear objective is maximal
does not change under small perturbations of the objective — is proved from LP
duality and strict complementarity without Minkowski–Weyl
([36b30e1](https://github.com/carlok/prove2me-logs/commit/36b30e1)). All six
theorems of the paper are now proved on the board, each accepted on its first
submission.
