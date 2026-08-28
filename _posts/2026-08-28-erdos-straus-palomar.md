---
title: "erdos-straus-offset-lean: a Palomar submission surface, checked by two kernels"
date: 2026-08-28
tags: [lean4, math, tool]
---

[erdos-straus-offset-lean](https://github.com/carlok/erdos-straus-offset-lean) now
carries a Palomar submission surface on its `palomar` branch: a
`Challenge.lean` statement surface, a `Solution.lean` with the proved
counterparts, and a comparator that audits the pair, pinned to Lean/Mathlib
v4.32.0. The Comparator result recorded in `formalization.yaml` passed on both
kernels — Lean's default kernel and the independent NanoDa kernel accept the
four compared theorems, with the axiom closure limited to `propext`,
`Classical.choice`, and `Quot.sound`. The metadata file also declares the
automation method as an agent (Claude Opus 5 High via Claude Code).
