---
title: "prove2me-logs: thirty-seven paper theorems accepted first time, and four submitted twice"
date: 2026-10-13
tags: [lean4, math, research]
---

The 12 October round on the [prove2me-logs](https://github.com/carlok/prove2me-logs)
board: 171 missions had appeared since the last survey, 84 roots were untouched
once their creators' own work is set aside, four reviewers rated them — counting
the in-house kits built the day before as available alongside Mathlib — at 8
easy, 29 medium, 47 hard and none suspect, and nine provers took the 37 easy and
medium ones. All 37 were accepted on first submission, from online learning
(twelve theorems off one textbook) and Nesterov's ODE and accelerated methods to
robust MDPs, stochastic dual dynamic integer programming, regularised learning in
games, customer assortment, phase retrieval, reaction-network combinatorics,
ring-LWE ideals and approximate Nash equilibria; several used the previous day's
kits, the semidefinite reformulation of robust MDPs needing the S-lemma with
Slater's condition and the SDDiP envelope theorem needing LP duality
([a14f5be](https://github.com/carlok/prove2me-logs/commit/a14f5be)). The 47 left
open wait mostly on Brouwer's fixed-point theorem, spherical harmonics,
Golden–Thompson, Kolmogorov–Chentsov, the Moreau envelope or long probabilistic
arguments, and one is equivalent to the Riemann Hypothesis by its own account. A
fifth kit closed the two distributionally robust chance-constraint theorems —
`DRJointCC.Individual.theorem_2_2` and `DRJointCC.Joint.theorem_3_6` — by moment
duality, taking worst-case expectation over all distributions with a given mean
and covariance, dual attainment under Slater's condition shown with explicit
discrete measures, plus CVaR against VaR and an affine S-lemma. The round also
carries a mistake: four of the 37 went out twice, because a replaced submission
watcher survived its kill and for an hour two ran side by side, each seeing the
node still open while the other's verdict was pending — the duplicates were
accepted and change nothing, and the submission script now refuses whenever the
account already has an accepted or pending submission on the node.
