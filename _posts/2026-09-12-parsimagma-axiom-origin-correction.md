---
title: "parsimagma: where the certificates' axioms actually come from"
date: 2026-09-12
tags: [math, research]
---

The certificates README in [parsimagma](https://github.com/carlok/parsimagma)
had the origin of its three permitted axioms wrong — they enter through the
`finOpTable` encoding, not through what `decide` invokes — and the
[correction](https://github.com/carlok/parsimagma/commit/2a75a1b) credits
Wenlin Zhang, who settled it by re-emitting 44 affine models as plain
arithmetic operations: same goal, same tactic, no axioms, 44/44 at carriers
2–9. The same README now records that the judge's default policy admits no
axioms at all, so the false column of the table fails under it while the true
column does not. The three Vampire proof logs were also republished with the
absolute working directory they had been produced in stripped out
([2f9bf2d](https://github.com/carlok/parsimagma/commit/2f9bf2d)) — the proofs
are worth publishing, the path they were written in is not.
