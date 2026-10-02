---
title: "LeanFrontier: a curvature-center tangency bridge from an outside contributor"
date: 2026-10-02
tags: [lean4, math, contribution]
---

The fork of
[qazW12345](https://github.com/qazW12345) — whose fork was the first thing I
wrote about in September — landed another slice of the corpus's Direction E
roadmap: a new `CurvatureCenter.Circle` carrying a curvature plus a Euclidean
centre in `ℂ`, a `bendCenter`, lossless conversions to and from
`EuclideanGeometry.Sphere ℂ`, an `IsExternallyTangent` equation in
reciprocal-curvature coordinates equivalent to Mathlib's `Sphere.IsExtTangent`,
and a Ford-circle specialization that recovers the accepted Farey-neighbour
cross-determinant criterion. The receiver accepted it — ordinary test, trusted
preflight, restricted formal validation, build, kernel recheck and downstream
import smoke all pass at the exact head — and it
[merged as PR #463](https://github.com/carlok/LeanFrontier/pull/463) into the
[LeanFrontier corpus](https://carlok.github.io/LeanFrontier/notes/). No new
mathematics is claimed: the module deliberately stops before any claim that the
algebraic Descartes Vieta reflection equals an inversive reflection, which the
roadmap requires a geometric configuration for first.
