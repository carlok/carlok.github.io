---
title: "diaz-modulus-lean: the companion note reaches 1.8, and Gelfond–Schneider is rebuilt as a tree of eleven nodes"
date: 2026-09-25
tags: [lean4, math, research]
---

Five more versions of the companion note to
[diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean) landed on 24
September, and the mirrored library grew with each.
[Version 1.4](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.4)
machine-checks the three barrier statements version 1.3 had proved on paper:
**the period never enters** (Theorem 5.6 — for `u` algebraically independent of
`π` the only quadratic relation with algebraic coefficients among `1, u, ū, iπ`
is the norm `X₁X₂ − ρX₀²`, so a configuration that could detect a candidate uses
the constant term, `u` and `ū` and never `iπ`), and Proposition 5.7 gives the
relations a non-generic candidate can carry. [Version
1.5](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.5) then
corrected 1.4's own claim that nothing known excludes a relation such as
`Re(u²) = π²`: Théorème 0.2 of Roy and Waldschmidt (1997), the quadric version of
the 1973–74 theorem, excludes every rational quadratic relation among `u, ū, iπ`
for a candidate algebraic over `ℚ(π)` with `Im u ∉ ℚπ`, and two more barrier
results followed (Theorems 5.4(c) and 5.6(c)).

[Version 1.6](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.6)
is the note after a reading of Diaz, Roy, Waldschmidt — books included — and
Dasgupta–Kakde: several results turn out to be classical or special cases of
published ones and are now attributed where they appear, the boundary section is
rewritten (over the algebraic span of 1 and the logarithms the rank inequality
alone would settle the question), item (2) of "what would have to be proved"
becomes Waldschmidt's strong five exponentials conjecture of 1988, and the
strong four exponentials conjecture is credited to Roy. Four node texts on the
platform carried false openness or novelty claims and were corrected in the same
pass. [Version
1.7](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.7)
machine-checks twelve results from that reading — the `e^{|λ|}` companion of Diaz
1997 Prop. 2 and Roy–Waldschmidt Cor. 7.4, Waldschmidt's LN 402 remark on pairs
of logarithms, and the fact that his strong five exponentials, sharp four
exponentials and 2×2 determinant conjectures each imply both Diaz's conjecture
and (S) — and [version
1.8](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.8) adds
rows for Diaz 1997 Proposition 1 and Waldschmidt's Consequence 1.6, proving its
intended Consequence 1.7.

The mirror closed at 239 of 239 by removing the last vendored module:
Gelfond–Schneider's single 5,388-line file is replaced by the tree published on
Prove2Me — 1,531 lines, Liouville's inequality and the first non-vanishing
exponential sum, eight steps behind the criterion, and the theorem assembled from
them under the same name
([d6f7a41](https://github.com/carlok/diaz-modulus-lean/commit/d6f7a41)) — a
restructuring of the formalization of Karatarakis and Wiedijk.
[prove2me-logs](https://github.com/carlok/prove2me-logs) records the same day
from the other side, correction notes on the entries whose claims the literature
reading overturned, and an entry that measures whether being imported actually
pays ([d5b2290](https://github.com/carlok/prove2me-logs/commit/d5b2290)).
