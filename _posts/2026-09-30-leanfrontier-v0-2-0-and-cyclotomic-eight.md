---
title: "LeanFrontier v0.2.0, and a day of cyclotomic-eight submissions"
date: 2026-09-30
tags: [lean4, math, project]
---

[LeanFrontier](https://github.com/carlok/LeanFrontier) shipped
[v0.2.0](https://github.com/carlok/LeanFrontier/releases/tag/v0.2.0), its first
library release since v0.1.1's two modules: 102 accepted modules on Lean and
Mathlib v4.34.1 across 15 top-level areas, nine modules deep at its longest
import chain, with the Markov uniqueness conjecture stated formally and one
classical coprimality hypothesis resolved by a formal computation of two rings
of integers. Admission is still mechanical and grew with what went wrong in
practice — kernel re-check by `leanchecker`, no build- or import-time code,
add-only submissions, and conjectures as a first-class quota-limited kind. The
same day a batch of outside submissions from
[@qazW12345](https://github.com/qazW12345) landed: the eighth cyclotomic
field's Galois group identified as a Klein four group
([#445](https://github.com/carlok/LeanFrontier/pull/445)), the missing Gaussian
quadratic direction added
([#446](https://github.com/carlok/LeanFrontier/pull/446)), and exactly three
quadratic intermediate fields proved, which completes that thread
([#456](https://github.com/carlok/LeanFrontier/pull/456)); topological
transitivity for the full tent map, transported through the accepted Ulam
homeomorphism to the parameter-four logistic map
([#444](https://github.com/carlok/LeanFrontier/pull/444)); the first cofinality
bridge between the corpus's Furstenberg topology and Mathlib's generic
profinite-completion indexing category
([#443](https://github.com/carlok/LeanFrontier/pull/443)); and Descartes
curvature reflections bundled into an algebraic action layer
([#457](https://github.com/carlok/LeanFrontier/pull/457)). The evidence ships
beside the code, including the citable
[corpus-v1](https://github.com/carlok/LeanFrontier/releases/tag/corpus-v1)
dataset snapshot; the running record is at the
[field notes](https://carlok.github.io/LeanFrontier/notes/).
