---
title: "An external check: fifty pairs agreed, two numbers did not"
date: 2026-09-03
tags: [lean4, math, research]
---

After [parsimagma](https://github.com/carlok/parsimagma) went public, someone
read it properly.

Wenlin Zhang took the fifty order-5 implications I had reported — magma law
pairs outside the Equational Theories Project's own graph, so with no published
answer to check against — and ran them through a completely independent solver
and corpus. Same verdicts on all fifty: the same 25 proved, the same 25
refuted. Two engines sharing only the problem statement and the Lean kernel.

That is worth more than what I had before. Two runs of my own program agreeing
with each other is a test of determinism, not of correctness. One run of
somebody else's program agreeing is evidence.

Then he found two numbers I had wrong.

**A denominator mismatch.** One document argued a floor of 385 implications
requiring infinite countermodels. Days earlier I had computed the exact split
from the ETP's closed implication graph — 610 infinite-only, 450 finite, 2 open
— written it up in a second document, and left the first one standing with its
older argument intact. He read a file that contradicted its own repository. The
floor argument is now kept explicitly as how the question looked before the
graph was fetchable, with his own dual-orbit numbers recorded alongside it.

**A grid quoted where the evidence was meant.** I had written that a negative
result about abelian extensions was decided across 661,142 fibre candidates.
That is the size of the search space before filtering. What actually survives
filtering is 2,147 fibres, and the negative rests on 55,516 decided settings.
The large number sizes the search; only the small one supports the claim. Both
are now stated separately, because quoting the first where the second belongs
inflates the result by two orders of magnitude.

He also pointed out that the certificates as I first published them could not be
re-audited — results without their sources. They are now at
[`dist/solo/certificates/`](https://github.com/carlok/parsimagma/tree/main/dist/solo/certificates):
all 200 with the Lean they were built from, and the fifty order-5 ones
re-elaborated through the judge after the fact, each carrying a status and an
`#print axioms` report. Fifty accepted, twenty-five closing over nothing,
twenty-five over the three the judge permits. Toolchain pinned in the README.
That was an oversight rather than a decision, and it is fixed.

None of this touched a verdict. The solver's results held under an independent
engine. What broke was my own bookkeeping about them, which is the part nobody
re-derives and everybody quotes.

He was not a disinterested reader. Wenlin Zhang, Haobo Ma and Manuel Israel
Cázares entered the same competition, and their
[solver](https://github.com/the-omega-institute/sair-eqt2-stage2-solver) is
broader than mine: 1889/1889 on the full public suite, 800/800 across the four
evaluation categories, 100/100 on the Marathon track, 200/200 on the stress
test, frozen five days before the deadline and never touched again. Their system
description is [arXiv:2609.00706](https://arxiv.org/abs/2609.00706). A
competitor spent an evening verifying fifty of my results and reading my
documentation closely enough to catch two inflated figures in it.

This is the part open science actually pays for, and it is not the part I
expected. Publishing the code gets you read. Publishing the numbers gets you
checked. Publishing the sources under the numbers is what makes being checked
possible at all, and that is exactly the piece I had left out.

All three points are now credited by name in the
[write-up](https://doi.org/10.5281/zenodo.22214743), which has an
acknowledgements section it did not have a week ago.
