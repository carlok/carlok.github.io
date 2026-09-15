---
title: "prove2me-logs: four exponentials gets a tree, its first leaf closes, and the zero count's source has a hole"
date: 2026-09-15
tags: [lean4, math, prove2me]
---

The Sep 14–15 entries in [prove2me-logs](https://github.com/carlok/prove2me-logs)
open a subtree under `four_exponentials_trdeg_one`, the one Open leaf of the
Diaz mission that is a theorem in the literature: six new nodes joined by three
accepted reductions
([b4002e2](https://github.com/carlok/prove2me-logs/commit/b4002e2)), routed
through Waldschmidt 1973 with two tools from his 1971 paper after reading and
rejecting the two Roy–Waldschmidt proofs. Transcribing the statements from page
images rather than the text layer caught a missing hypothesis (`σ₂ ≤ σ₁`) and a
wrong exponent, and the lattice step forced one classical fact out into a node
of its own — an exponential polynomial with distinct frequencies does not vanish
identically — which closed as the branch's first leaf
([f8f57d7](https://github.com/carlok/prove2me-logs/commit/f8f57d7)).

Then the zero count split, and the audit turned up something worth writing down
([d72e159](https://github.com/carlok/prove2me-logs/commit/d72e159)): Waldschmidt
1971 §4 Lemma 3 reaches its published bound through `n!·2ⁿ ≤ nⁿ`, which is
false for n ≤ 5, and for n = 2 the paper's choice of radius genuinely fails over
part of the range. The bound survives — optimising the radius from the paper's
own inequality (4.14) reproduces it for every n from 2 to 10⁵ — but a formal
proof has to choose the radius differently for small n, which is now stated as
the open child's job. Both small leaves were proved the same day, and the
library on GitHub holds 139 of 139 Proved results.
