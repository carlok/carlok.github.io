---
title: "diaz-modulus-lean: Waldschmidt's 1973 theorem is machine-checked, and Schneider's eighth problem with it"
date: 2026-10-01
tags: [lean4, math, research]
---

The Diaz companion note reached
[v1.12](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.12):
Waldschmidt's 1973 theorem in its algebraic-independence form is now
machine-checked — if `x₁, x₂` and `y₁, y₂` are linearly independent over `ℚ` and
`e^(x₁y₂)`, `e^(x₂y₂)` are algebraic, then two of the eight numbers `x_i`, `y_j`,
`e^(x_iy_j)` are algebraically independent
([8b015b3](https://github.com/carlok/diaz-modulus-lean/commit/8b015b3)) — formalised
as a one-column extension of the four exponentials development rather than a new
development of its own. That closes what the
[previous version](/blog/2026/09/30/diaz-modulus-lean-note-1-11-size-wave-5/) had
to carry as a hypothesis: the consequence added in v1.11 is unconditional,
Section 4 no longer says the theorem is not formalised, and the status *"Proved,
assuming Waldschmidt 1973"* is gone from Appendix A. It brings Schneider's
eighth problem — at least one of `e^e` and `e^(e²)` is transcendental — and the
`e^(π²)` statement with it. No new mathematics is claimed, the mirrored library
stands at 283 results, and
[prove2me-logs](https://github.com/carlok/prove2me-logs) carries the same day
from the research side
([22c5195](https://github.com/carlok/prove2me-logs/commit/22c5195)).
