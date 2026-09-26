---
title: "diaz-modulus-lean: companion note 1.9, and three size waves that turn 2,865 lines into 856"
date: 2026-09-26
tags: [lean4, math, research]
---

The companion note to
[diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean) reached
[version 1.9](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.9),
which checks Appendix A statement by statement against the Lean nodes: four rows
whose proofs take Baker's theorem on linear forms in logarithms as a hypothesis
are now marked "Proved, assuming Baker" and Section 1 lists that theorem as a
third input used without proof, Corollary 3.4 is marked Not formalised because
no node states it, Proposition 3.2 is restated as
`Diaz.quantisation_orbit_iff_re_ne_zero` proves it, and all 81 identifiers match
the platform, the mirror holding 254 results.

Three "size waves" the same day moved proof text that had been carried inline
into nodes published on Prove2Me and mirrored back. The
[first](https://github.com/carlok/diaz-modulus-lean/commit/b0cbcfd) turned four
general results into nodes and gave nine others second proofs that import them,
taking 2,865 lines to 856. The
[second](https://github.com/carlok/diaz-modulus-lean/commit/d09d7ad) replaced the
single 1,550-line proof of `aligned_norm_free_no_rational_log_matrix` with 44
lines over three new nodes, its four dependent proofs going from 2,725 lines to 320.
The [third](https://github.com/carlok/diaz-modulus-lean/commit/09c2ded) split the
1,046-line helper block that Waldschmidt's Lemmas 4 and 7 each carried into eight
nodes, taking the two proofs from 4,068 lines to 458.
[prove2me-logs](https://github.com/carlok/prove2me-logs) records the same work
from the platform side
([94ce1bc](https://github.com/carlok/prove2me-logs/commit/94ce1bc),
[c0f28eb](https://github.com/carlok/prove2me-logs/commit/c0f28eb),
[9be3b9b](https://github.com/carlok/prove2me-logs/commit/9be3b9b)).
