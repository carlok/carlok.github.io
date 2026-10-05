---
title: "lspace-det-sigma: an L-space knot inequality, a data policy, and a Lean 4 lattice lemma"
date: 2026-10-05
tags: [math, lean4, research]
---

[lspace-det-sigma](https://github.com/carlok/lspace-det-sigma) asks whether `det(K) ≤ 1 + |σ(K)|` for every L-space knot — a conjecture found by a program that fits linear inequalities to a table of knot invariants and discards what its own checks refute, not a theorem except where stated. The note proves it for every iterated torus knot, hence every algebraic knot, by induction over cabling with Litherland's formula and the bound `|σ(T(p,q))| ≥ g(T(p,q))`, proved here from the lattice count for torus knot signatures; the combinatorial core of that lemma — `N_< ≤ (p−1)(q−1)/8` for `2 ≤ p < q` — is formalised in Lean 4 with no `sorry`, on `propext`, `Classical.choice` and `Quot.sound` alone. The hyperbolic case, where the inequality is sharp, stays open. KnotInfo is cited as its maintainers ask — cited, not copied, since a copy of the database goes out of date — at the two places the note relies on it, and `DATA.md` and the README give that reason for its absence ([dfec446](https://github.com/carlok/lspace-det-sigma/commit/dfec446)); a later commit sharpens the same file without quoting the correspondence ([cc42290](https://github.com/carlok/lspace-det-sigma/commit/cc42290)).
