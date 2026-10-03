---
title: "diaz-modulus-lean: note v1.16 proves Baker's theorem, and Diaz's (Qr2) in transcendence degree one"
date: 2026-10-03
tags: [lean4, math, research]
---

The Diaz companion note reached
[v1.16](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.16), where
[Baker's theorem](https://github.com/carlok/diaz-modulus-lean/commit/3b9662a) is
proved rather than assumed: ℚ-independent logarithms of algebraic numbers are
linearly independent over ℚ̄, along the Bertrand–Masser route through the
Schneider–Lang criterion for `ℂ^{d₀} × (ℂ^×)^{d₁}` with `d₀ <= 1` and a Schwarz
lemma for Cartesian products — so the four appendix rows that had read "Proved,
assuming Baker" now name unconditional forms. A new subsection, "Products on the
axes", adds Diaz's conjecture (Qr2) of 2007 in transcendence degree one
(Proposition 6.11, Theorem 6.12, Corollary 6.13), by running Diaz's own argument
with the four exponentials theorem in degree one in place of the conjecture, and
the title of Brownawell's 1974 paper is corrected. The appendix was checked
against the live board (115 identifiers, no mismatch) and the library now holds
all 340 proved results on Lean's three standard axioms;
[prove2me-logs](https://github.com/carlok/prove2me-logs) carries the same day from
the research side, down to Baker's theorem as a hypothesis discharged
([8c8d14b](https://github.com/carlok/prove2me-logs/commit/8c8d14b)). The same
batches published the
[blueprint site](https://carlok.github.io/diaz-modulus-lean/), which states each
classical theorem with a dependency graph, links to the declaring line of the
Lean source and a PDF
([af4f944](https://github.com/carlok/diaz-modulus-lean/commit/af4f944)), and
refuses to build an incomplete site
([e807733](https://github.com/carlok/diaz-modulus-lean/commit/e807733)).
