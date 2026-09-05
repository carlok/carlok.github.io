---
title: "magma-1518-obstruction-lean: one-generated 1518-magmas, and a cohomology wall"
date: 2026-09-05
tags: [lean4, math, research]
---

[magma-1518-obstruction-lean](https://github.com/carlok/magma-1518-obstruction-lean)
is a new public Lean 4 repository about the Equational Theories Project law
1518, `x = (y ◇ y) ◇ (x ◇ (y ◇ x))`. It proves that every one-generated magma
satisfying 1518 and 3862 is trivial or the Z/3 shift — Terence Tao's
conjecture from the November 2024 Lean Zulip, now without a finiteness
assumption and with a single target law — where the core table-and-closure
argument carries no axioms. A second result shows constant-coefficient magma
cohomology cannot refute `1518 ⇒ 47, 614, 817, 3862` from any finite base:
`H²` vanishes over the shift, so every such extension is a direct product. The
README states the full theorem set (A–E) with a per-statement tally of
confirming tools — core Lean, Vampire, Mace4, z3, brute force — and notes the
repository claims no new implication, since the ETP has settled them all.
