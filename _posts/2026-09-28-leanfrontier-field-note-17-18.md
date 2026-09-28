---
title: "LeanFrontier: the same fact twice, and a lemma of its own (Field Notes 17 and 18)"
date: 2026-09-28
tags: [lean4, math, project]
---

Two [Field Notes](https://carlok.github.io/LeanFrontier/notes/) landed in two
days. [Field Note 17](https://carlok.github.io/LeanFrontier/notes/field-note-17.html)
— "The Same Fact, Twice" — has the Srinivasan collision identity coming back
after the previous note recorded it lost, and then two submissions opened
**forty-six seconds apart from the same fork**, both proving that `−1` is a
square modulo every Markov number: the first in the integers modulo `m` via
Mathlib's primitive sums of two squares, the second as the existence of `r`
with `r² ≡ −1 (mod m)` via a Bézout lemma the same contributor had landed that
evening. The receiver accepted both, correctly by its own rules — it compares
each statement with Mathlib and the corpus exactly, and two notations for one
fact are two statements to it — so the corpus now holds a result twice, and the
only reason anyone knows is that a person read both. The same note extends the
deepest chain in the corpus to nine modules.

[Field Note 18](https://carlok.github.io/LeanFrontier/notes/field-note-18.html)
— "One Lemma of Its Own" — builds the prime-power step on that collision
identity: if `pᵏ` divides a shared Markov coordinate, `p²ᵏ` divides one factor
entirely, which is the arithmetic core of the elementary proofs that a Markov
number which is a prime power determines its triple. Of the six Markov
submissions merged since Friday, five say in their own claims that the
mathematics is not new, and they are right; the sixth is the
[gcd identity posted
yesterday](/blog/2026/09/27/leanfrontier-markov-slope-scale-gcd/), the piece
nothing depends on. Three classical-geometry submissions then landed in one
afternoon, all from the fork of [qazW12345](https://github.com/qazW12345):
[the Weitzenböck inequality](https://github.com/carlok/LeanFrontier/pull/404),
[Euler's quadrilateral
theorem](https://github.com/carlok/LeanFrontier/pull/405) and [Varignon's
theorem](https://github.com/carlok/LeanFrontier/pull/413), the last stated as
equality of both pairs of opposite side vectors of the midpoint parallelogram.

On the maintainer's side, the catalogue's import graph is now drawn with
Graphviz, one `dot` drawing per connected group of modules, because a flat
graph was unreadable at 92 modules
([#406](https://github.com/carlok/LeanFrontier/pull/406)) — and the merge queue
got the fix for a failure that could never be seen: `gh pr checks` exits `1`
when any check has failed, so under `set -o pipefail` the queue's own pipeline
died before its `grep` could report the failing check, which is why one pull
request waited out its full hour and then looped on an expired token
([#410](https://github.com/carlok/LeanFrontier/pull/410)).
