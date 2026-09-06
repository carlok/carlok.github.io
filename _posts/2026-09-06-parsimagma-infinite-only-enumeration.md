---
title: "parsimagma: the 820 infinite-only pairs, enumerated"
date: 2026-09-06
tags: [math, research]
---

[parsimagma](https://github.com/carlok/parsimagma) now
[enumerates, pair by pair](https://github.com/carlok/parsimagma/commit/2e53f04),
every implication that is false in general but holds for every finite magma:
820 ordered pairs — 610 from the unresolved hard core and 210 from the
saturation-refuted set — decoded from the ETP's closed implication graphs into
`data/etp/infinite-only.tsv`. The exact split answers the question left open
in the project's
[#1474](https://github.com/teorth/equational_theories/issues/1474), and it
makes the corpus's coverage readable honestly: 610 of the 1062 hard-core pairs
can never be refuted by a finite construction, so the real figure is 411 of
the 450 finitely refutable (91%), with the remaining 39 listed. A differential
test against the ETP's Lean-verified finite graph agrees on all 797 finite
claims.
