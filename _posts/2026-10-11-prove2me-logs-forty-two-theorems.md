---
title: "prove2me-logs: forty-two paper theorems in one night, all accepted first time"
date: 2026-10-11
tags: [lean4, math]
---

A day after [the first round](/blog/2026/10/09/prove2me-logs-nineteen-theorems-one-false/),
the [prove2me-logs](https://github.com/carlok/prove2me-logs) board recorded a
second: 200 more single-theorem paper missions had appeared, mikedeng1 had
published 150 that nobody had touched and Mazecto two more, and over a field of
152 roots with 265 definitions behind them six reviewers read every statement
together with its definitions — 5 easy, 37 medium, 110 hard, none suspect —
before six provers took the 42 easy and medium ones, grouped by paper so that
one descent lemma or one cone lemma served a whole family, and submitted them
one at a time with a written explanation of the argument
([c4422cd](https://github.com/carlok/prove2me-logs/commit/c4422cd)). All 42 were
accepted, each on its first submission, from accelerated methods and their ODEs
through splitting and constraint qualifications to pricing, online learning,
matrix relaxations and integer programming.

The 110 left open mostly wait on theory Mathlib does not have yet: Brouwer and
Kakutani fixed points, the existence of Brownian motion and Itô calculus, conic
and SDP duality with the S-lemma, the Moore–Penrose inverse, Opial's lemma,
Kolmogorov–Chentsov, and Sierpiński's intermediate-value theorem for atomless
measures. Two pieces were built inside proofs because they were missing, and
both would be small, useful additions: closedness of finitely generated cones,
hence a finite Farkas lemma, and the fact that covers generate a finite strict
order. The false statement from the first round,
`SymPolyOpt.PowerSumUB.theorem_6_7`, now reads `Disproved` on the board,
completing [the notification written up yesterday](/blog/2026/10/10/prove2me-logs-false-statement-notified-disproved/).
