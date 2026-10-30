---
title: "LeanFrontier: the discrete Lagrange–Green identity, with forcing, in any commutative ring"
date: 2026-10-29
tags: [lean4, math]
---

[#546](https://github.com/carlok/LeanFrontier/pull/546) proves the discrete Lagrange–Green identity for two *forced* solutions of a second-order recurrence with variable coefficients: with `u(n+2) = p n·u(n+1) − q n·u n + f n` and `v` driven by `g`, the Casoratian satisfies `D(n+1) = q n·D n + u(n+1)·g n − f n·v(n+1)`, and unrolling it gives the closed Green-source sum — `D n = (∏ i<n, q i)·D 0 + ∑ j<n (∏ j<i<n, q i)·(u(j+1)·g j − f j·v(j+1))` ([b52dee6](https://github.com/carlok/LeanFrontier/commit/b52dee6)).

Three entrypoints carry it: `affine_recurrence_eq_sum_prod` for the nonautonomous affine recurrence, `casoratian_forced_succ` for the one-step identity, and `casoratian_forced_eq_sum_prod` for the formula. The proof is division-free — no inverse of any recurrence coefficient, so zero divisors and degenerate cases are covered — and it generalises the accepted homogeneous `casoratian_succ` of [Field Note 27](/blog/2026/10/20/leanfrontier-field-note-27-casoratian/) rather than duplicating it, which is exactly the consumption the series measures. Mathlib's ordered-semiring discrete Gronwall inequality is related but not this ring-valued exact statement.

The submission by [qazW12345](https://github.com/qazW12345) is two added files and no modification to any accepted one, machine-authored by GPT-6 on Mathlib `v4.35.0`, and it passed the fork's trusted receiver with `accepted: true` and empty diagnostics before the receiver merged it on 2026-10-29. Field notes are at [carlok.github.io/LeanFrontier/notes](https://carlok.github.io/LeanFrontier/notes/).
