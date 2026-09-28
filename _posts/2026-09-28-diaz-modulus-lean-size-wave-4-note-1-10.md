---
title: "diaz-modulus-lean and prove2me-logs: the fourth size wave, and companion note 1.10 withdraws a priority claim"
date: 2026-09-28
tags: [lean4, math, research]
---

The companion note to [diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean)
reached [version 1.10](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.10)
to **withdraw a claim the note should not have made**: Section 6 called the
transcendence degree two of two unrelated candidates of commensurable moduli
"the first constraint of any kind on such families", and Diaz 2007, Corollaire
4(2) — a consequence of Roy's strong six exponentials theorem — already puts one
of `u/v`, `v/u` outside the algebraic span of `1` and the logarithms for such a
pair. The sentence now cites it, all 81 identifiers match the platform, and the
mirror holds 262 results
([c04cf7a](https://github.com/carlok/diaz-modulus-lean/commit/c04cf7a)).

A fourth size wave took the last proofs of 300 lines or more and turned them
into reductions to general nodes
([b491c6a](https://github.com/carlok/diaz-modulus-lean/commit/b491c6a)): eight
new results — Siegel's lemma with an entrywise bound, the Cauchy estimate on a
grid, the four exponentials extrapolation inequality, Liouville through the
resultant, the multiplicative step of Gel'fond's lemma, the monic integral model
and two denominator-house bounds — with second proofs of `extrapolation`,
`siegel_aux`, `small_irreducible_factor`, `trdeg_one_presentation`,
`SX.descent_step` and `SX.exists_aux_expSum` going from 2,661 lines to 906, and
the mirror still at 262 of 262.
[prove2me-logs](https://github.com/carlok/prove2me-logs) records it from the
platform side and publishes the nodes parents-first, so seven of them joined the
mission while still Open
([3c927df](https://github.com/carlok/prove2me-logs/commit/3c927df)), then
corrects its own milestones entry — the first version had inferred a counting
rule from a mission board that turned out to be a cached snapshot
([ad47f59](https://github.com/carlok/prove2me-logs/commit/ad47f59)) — and links
the 21 theorems that are milestones of the mission
([5ef3601](https://github.com/carlok/prove2me-logs/commit/5ef3601)).
