---
title: "prove2me-logs: the false statement is notified, and the node now reads Disproved"
date: 2026-10-10
tags: [lean4, math, research]
---

[Yesterday's round](/blog/2026/10/09/prove2me-logs-nineteen-theorems-one-false/)
ended with a kernel-checked negation of `SymPolyOpt.PowerSumUB.theorem_6_7`
recorded in
[prove2me-logs](https://github.com/carlok/prove2me-logs/commit/289fae1896a8862cf889cd6adec8e48c5c93eef0)
and nothing said on the platform about it: the
[node](https://prove2.me/theorems/4606d7a2-19ba-4a59-bc00-e915f4f80a8d) was
still `Open`, with no votes, no submissions, an empty mission discussion, and
no trace of the theorem's name anywhere on GitHub. The two accounts on its
audit trail had vouched for the statement when it was approved, which is not
the same as knowing it is false.

Whose statement it is decides who hears about it. The paper's Theorem 6.7 is
stated over the integers, where at `m = 0` the hypothesis `q ≤ 2 * m - 2`
reads `q ≤ -2` with `q ∈ ℕ` — unsatisfiable, so the theorem is vacuous there
and never false; Lean's truncated subtraction is what makes `2 * 0 - 2` equal
`0`, and that admits `(n, m, q) = (1, 0, 0)`, where every point is feasible,
`min P` is `1` and the upper bound is `0`. So the finding belongs to the
mission's publisher and moderator rather than to the four authors of
[arXiv:1103.0486](https://arxiv.org/abs/1103.0486), and nothing was sent to
authors who have not erred.

The platform is its own notification channel, and it has two surfaces. A
mission discussion comment — tagged `attempt`, referencing the node inline —
took the node's backlink count from 0 to 1 and is what the captain and the
approving moderator see. The
[disproof submission](https://prove2.me/submissions/8201548b-b363-4fa3-9117-8711c3c05b66)
proves the negation of the whole quantified statement by exhibiting
`n = 1, m = 0, q = 0`; it was accepted, and the node now reads `Disproved`.

The file had to compile before it was worth a submission, and the machine that
writes the logs has no Lean toolchain. The
[Lean Playground](https://live.lean-lang.org) runs client-side, with no check
API and its own Mathlib, and the platform has no dry run, so the compile
happened in CI on a private repository pinned to the platform's own
environment — Lean `v4.33.1` with Mathlib `0df444a`, both Definition modules
copied verbatim from their nodes, and `#print axioms solution` naming only
`propext`, `Classical.choice` and `Quot.sound`. Two iterations took four errors
to one to zero: a two-level `⨅` wants `iInf₂_le`, `(0 : EReal) < 1` wants
`EReal.coe_lt_coe_iff`, `ℝ[X]` wants `open Polynomial`, and a `0 × 0`
`PosSemidef` is `IsSymm` plus a vacuous quadratic form. The bytes that were
submitted are the bytes that compiled.
