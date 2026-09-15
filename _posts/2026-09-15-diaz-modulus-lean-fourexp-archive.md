---
title: "diaz-modulus-lean: the four exponentials subtree archived and mirrored, and the zero count reduced"
date: 2026-09-15
tags: [lean4, math, research]
---

[diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean) now holds the
four-exponentials branch instead of citing it: the `FourExp` nodes are archived
alongside the Diaz ones
([3d5d9ce](https://github.com/carlok/diaz-modulus-lean/commit/3d5d9ce)) with the
reduction sketch and its pieces
([57f3ec7](https://github.com/carlok/diaz-modulus-lean/commit/57f3ec7),
[6714dcb](https://github.com/carlok/diaz-modulus-lean/commit/6714dcb)), the
refresh script searches the `FourExp` namespace too
([ab6aa90](https://github.com/carlok/diaz-modulus-lean/commit/ab6aa90)), and
each Open node's formal statement and write-up is now mirrored into
`archive/prove2me/open` — rewritten when the board changes, deleted once the
node stops being Open, and covered by `--check`
([3eb78a7](https://github.com/carlok/diaz-modulus-lean/commit/3eb78a7)).

Two results followed. `FourExp.expPoly_ne_zero` — an exponential polynomial with
distinct frequencies is not identically zero — was accepted on Prove2Me,
archived and ported, taking the library to 137 of 137 Proved results closing over
only Lean's three axioms
([5812224](https://github.com/carlok/diaz-modulus-lean/commit/5812224)). The zero
count was then archived as a reduction with its four children
([dfc9853](https://github.com/carlok/diaz-modulus-lean/commit/dfc9853),
[f62c6b5](https://github.com/carlok/diaz-modulus-lean/commit/f62c6b5)), two of
which are proved — `zero_count_arith_poly` and `zero_count_degenerate`, both
accepted on Prove2Me and ported
([47957bc](https://github.com/carlok/diaz-modulus-lean/commit/47957bc)) — for
139 of 139 Proved results in the library.
