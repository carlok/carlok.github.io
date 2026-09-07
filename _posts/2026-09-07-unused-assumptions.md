---
title: "unused-assumptions: Mathlib theorems whose typeclass setting is stronger than their proof"
date: 2026-09-07
tags: [lean4, math, research]
---

[carlok/unused-assumptions](https://github.com/carlok/unused-assumptions) is a
new public repository (visible since Sep 4; v1.0–v1.2 tagged Sep 6, archived at
[doi:10.5281/zenodo.22549525](https://doi.org/10.5281/zenodo.22549525)):
theorems in Mathlib whose stated algebraic setting is stronger than their own
proof requires. The method is one sentence — take a theorem, replace one binder
with a weaker class, keep the proof byte for byte, compile it alone — and every
row of `data/survivors.jsonl` carries what is needed to put the claim back in
front of the compiler. A verifier rechecks each row at the Mathlib revision the
manifest names, refuses to run against a different one, and requires
`#print axioms` to rest on nothing beyond `propext`, `Classical.choice` and
`Quot.sound`. Re-verifying the 36 candidate patches against a later Mathlib kept
the [33 that still hold](https://github.com/carlok/unused-assumptions/commit/cf8eb65),
and the README now answers the prior-art question explicitly rather than leaving
it to the reader.
