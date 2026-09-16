---
title: "diaz-modulus-lean: the four-exponentials leaves close and the transcendence criterion is machine-checked"
date: 2026-09-15
tags: [lean4, math, research]
---

The four-exponentials branch of
[diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean) went from a
tree of Open nodes to a closed criterion, in a sequence of archive-and-port
steps: the transcendence criterion reductions and their children were mirrored
([707c4d2](https://github.com/carlok/diaz-modulus-lean/commit/707c4d2)), then
the 1973 construction reduction and its four children
([e79b003](https://github.com/carlok/diaz-modulus-lean/commit/e79b003)), and
then the leaves were proved one at a time, each archived, ported and dropped
from `open/`:

- Gel'fond's height bound for a divisor, from Mathlib's Mahler measure
  ([a3cd190](https://github.com/carlok/diaz-modulus-lean/commit/a3cd190));
- the resultant bound of the 1971 proof, read off the Sylvester adjugate and
  bounded entry by entry with the Leibniz expansion, since Mathlib has the
  Bézout identity but not Hadamard's inequality
  ([b52f764](https://github.com/carlok/diaz-modulus-lean/commit/b52f764));
- the Cauchy estimate with zeros, accepted twice because the first accepted
  sketch used two lemmas absent from the mirror's Mathlib v4.32.0, so the
  version that proves them locally is the one ported
  ([8043e3d](https://github.com/carlok/diaz-modulus-lean/commit/8043e3d));
- the radius in the zero count, now `u = max(n^λ, 3)`, which avoids the 1971
  step `n!·2ⁿ ≤ nⁿ` that is false for `n ≤ 5` — the hole flagged in the
  previous post ([ca756e0](https://github.com/carlok/diaz-modulus-lean/commit/ca756e0));
- `expPoly_value_le_derivs`, which by cascade made
  `expPoly_zero_count_scaled`, `expPoly_zero_count` and
  `nonvanishing_derivative` Proved on the platform, their accepted sketches
  ported as they stood
  ([a48c4fc](https://github.com/carlok/diaz-modulus-lean/commit/a48c4fc),
  [7ea8f4f](https://github.com/carlok/diaz-modulus-lean/commit/7ea8f4f)).

The last open lemma was Gel'fond's small irreducible factor — reconstructed
rather than cited, since the paper points at Gel'fond and Lang and neither
proof is in hand — proved through the Roy–Waldschmidt 1997 Corollary 3.7
resultant bound written out over the roots, which completed the sketches of
`transcendence_criterion_continuous` and `transcendence_criterion` and closed
the branch ([bc7f999](https://github.com/carlok/diaz-modulus-lean/commit/bc7f999)).
Everything in the sequence rests on nothing beyond `propext`,
`Classical.choice` and `Quot.sound`.
