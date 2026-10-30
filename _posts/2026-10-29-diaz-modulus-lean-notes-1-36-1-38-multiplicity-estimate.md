---
title: "diaz-modulus-lean: notes v1.36–v1.38 machine-check Roy's six exponentials from a multiplicity estimate, then discharge its one open hypothesis"
date: 2026-10-29
tags: [lean4, math, research]
---

Three rounds on 29 October took [diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean) from 503 to 564 proved results, each released as its own version of the companion note: [v1.36](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.36) at 08:37, [v1.37](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.37) at 18:38 and [v1.38](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.38) at 19:46, with the appendix running from 221 to 224 checked identifiers ([7de8588](https://github.com/carlok/diaz-modulus-lean/commit/7de8588), [7be2496](https://github.com/carlok/diaz-modulus-lean/commit/7be2496), [9fcf00d](https://github.com/carlok/diaz-modulus-lean/commit/9fcf00d)).

**C1.4 — Roy's theorem, from a multiplicity estimate.** Twenty-six ported nodes prove the strong six exponentials theorem out of the elementary multiplicity estimate `hME`, whose architecture is the point: a coordinate complement of a rational span, a matrix whose vanishing maximal minors force a kernel vector, a left inverse for an integral-to-rational transfer, and the interpolation determinant that does the tangent counting. 529 of 529 results.

**C1.1 — the Hilbert side, under unmixedness.** Thirty nodes give the finite-level Hilbert-function layer of `hME` on the boxes of `K[X, Y, Z]` modulo the torus ideal of `𝔾ₐ^{A₀} × 𝔾ₘ^{A₁}` — the box filtration, its chain bound by a telescoping argument, and the torus reduction — with Macaulay's unmixedness carried as the explicit hypothesis `hU`, because nothing in the library proved it. 559 of 559.

**C1.2 — and then it is proved.** Five nodes settle the inequality half of Macaulay's unmixedness theorem for polynomial rings over an algebraically closed field (`DiazModulus.unmixedHeight_mvPolynomial`, after Macaulay 1916 and Bruns–Herzog Th. 2.1.6) by a local route through Matsumura Th. 17.2, Rees' characterisation of regular sequences via `Ext`, and the `Xᵢ − aᵢ` from the Nullstellensatz, so `torus_hilbert_side_complex` states the Hilbert side over `ℂ` with `hU` gone. 564 of 564.

What is left is stated rather than hidden: the multiplicity side of `hME`, and the assembly of `hME` from its two sides, so `hME` remains a hypothesis and Roy's theorem is still machine-checked only under it. The [prove2me-logs](https://github.com/carlok/prove2me-logs) board carries the same day from the research side, one entry per round ([43e542a](https://github.com/carlok/prove2me-logs/commit/43e542a), [1401299](https://github.com/carlok/prove2me-logs/commit/1401299), [6123d3f](https://github.com/carlok/prove2me-logs/commit/6123d3f)).
