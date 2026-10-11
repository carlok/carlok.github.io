---
title: "lspace-det-sigma: u = g for the Baker–Kegel and Himeno families, and a determinant that does not fix the signature"
date: 2026-10-11
tags: [math, research]
---

New note k32 in [lspace-det-sigma](https://github.com/carlok/lspace-det-sigma)
proves `u = g₄ = (m n² − n + 2)/2` for the closed 2n-braids `H(n,m) = X_n^m T_n`,
which contain the Baker–Kegel knots at `n = 2` and Himeno's knots at `m = 3`: the
lower bound is slice-Bennequin, the upper bound an explicit unknotting —
palindromic copies of `X_n` cancel in pairs, half of the last copy and one band
of `T_n` are flipped, and the leftover strands lie under everything — checked by
computer for `n ≤ 12`, `m ≤ 7`, and the same argument covers the non-positive
L-space `(2,q)`-cables of `T(2,2k+1)`
([162c38f](https://github.com/carlok/lspace-det-sigma/commit/162c38f)). The
mirror of `12n_642` is fibered and strongly quasipositive with `g = 2` and
`u ≥ 3`, so the L-space hypothesis is doing work; the literature check that
found it credited the example to Bode and Truol and the surrounding bounds to
Stoimenow, Kegel et al., Lidman–Moore, Baker–Moore, Hedden,
Borodzik–Liu–Zemke and Teragaito, and showed `g = g₄` for the whole family, not
only its L-space members
([71f08cb](https://github.com/carlok/lspace-det-sigma/commit/71f08cb)).

Revised k33: `Δ(K_k)` is the Alexander polynomial of the `(2,4k+5)`-cable of
`T(2,2k+1)` and `det(K_k) = 4k+5` for every `k`, with `σ(K_k) = −(4k+4)`
certified for `k ≤ 60`; grouping the 13,223 known L-space knots by Alexander
polynomial finds 37 groups carrying two signatures, so the signature is not a
function of the knot Floer complex. The note also corrects itself — an earlier
version said Himeno's `K₃ … K₈` are provably not braid positive, and Himeno
proves it for even `n` only. All 373 problems of Kirby's K3 list were then read:
none states `u = g` for L-space knots or bounds the determinant by the
signature, the closest is Problem 1.5 on genus and unknotting number, and the
inequality would touch Moore's conjecture, Problem 1.22
([eaa9f65](https://github.com/carlok/lspace-det-sigma/commit/eaa9f65)).
