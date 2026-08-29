---
title: "parsimagma: the hard core splits exactly, and a coverage number that was understated by its own denominator"
date: 2026-08-29
tags: [math, tool, research]
---

The Equational Theories Project's completed implication graph turns out to be
fetchable: `finite_graph.json` and `graph.json` are build artifacts the site
serves and the repository does not track, and decoding them reproduces the
project dashboard exactly, recovering its two remaining open cells,
`(677, 255)` and its dual, without being told. That splits the 1,062
Vampire-unresolved implications precisely — **610 require an infinite model,
450 have a finite counterexample, 2 are still open** — which settles the
question [parsimagma](https://github.com/carlok/parsimagma) had filed as
unanswerable in [issue #1474](https://github.com/teorth/equational_theories/issues/1474),
and corrects its own headline: 610 of those 1,062 admit no finite counterexample
at all, so the corpus reaches 411 of 450, not 411 of 1,062. Same measurement,
39% or 91% depending on which denominator you bother to compute. The earlier
claim that the circulating figure of 310 sits below a provable floor is
withdrawn: counted up to duality the same set is 316, so 310 looks like a
dual-class count against an earlier snapshot rather than an error. The graph is
also Lean-verified, so it can contradict the engine, and does not: 790 of 790
finite witnesses agree, and 19,392 order-5 laws extracted from a fork's branch
agree too.
