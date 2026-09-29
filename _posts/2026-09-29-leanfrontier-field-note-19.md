---
title: "LeanFrontier: an edge aimed at on purpose, and a corpus of 96 modules (Field Note 19)"
date: 2026-09-29
tags: [lean4, math, project]
---

[Field Note 19](https://carlok.github.io/LeanFrontier/notes/field-note-19.html) —
*Aimed at the Number* — opens with a submission that arrived ten hours after the
previous note's day
saying, in writing, that it had been **chosen to add an import edge**: the thing
the accumulation series counts had become something a producer aims at. The two
facts are about Varignon's parallelogram's perimeter — adjacent sides half the
diagonals, so the perimeter is their sum — and the import is genuinely used,
calls the corpus's Varignon theorem inside the proof. It was then rejected for
`RESOURCE_LIMIT_EXCEEDED`: the statement, fully expanded, is larger than what the
receiver will fingerprint and probe, and the mathematics was never in question.
The agent answered with five pushes in thirty-five minutes, each smaller, each
refused in the same words — because the diagnostic said the theorem "exceeds the
normalized-term limit", and *term* reads as the proof while the receiver only
ever measured the statement
([4c4210f](https://github.com/carlok/LeanFrontier/commit/4c4210f) now says which
term it measures, how large it is, and that the proof is not counted). The same
contributor closed the day with the first bridge between the corpus's
Stern–Brocot tree and the Euclidean algorithm — `k` identical turns along a path
record a quotient `k` of the algorithm, or `k + 1` if the path ends there — both
theorems stated in terms of `SternBrocot.pair`, a corpus constant that now
appears in the statements of six submissions, which is the catalogue measure that
cannot be moved cheaply. The corpus stands at 96 modules and 74 internal import
edges.

The weekly Mathlib check found v4.34.1 and then spent two attempts on it: the
first failed after fifty minutes leaving only an exit code, because the audit
wrote its reason into a file inside a container the workflow never copied out,
and the second built the corpus and stopped when the kernel re-check of one
module — the Markov descent step — ended without a word. Run by hand the same
check passes, and peaks at eight gigabytes, twice its neighbours, against a
container that allowed six, so the checker was killed for its size rather than
for anything it found and the container gets more room.

The morning's maintainer work points the same way: the corpus now exports as a
dataset, one record per accepted submission with the claim as submitted, the
accepting commit and date, the modules its merge added and the receiver
observation — 96 records for 96 claims in 130 KB, byte-for-byte reproducible at a
tag via the accumulation series' own first-parent walk
([e0addee](https://github.com/carlok/LeanFrontier/commit/e0addee)) — and the
receiver's reports are now aggregated weekly into rejection counts that count
only submission validations, after the first backfill buried 570 verdicts under
`NO_REPORT` for runs that never had one
([66545ba](https://github.com/carlok/LeanFrontier/commit/66545ba),
[72bf82a](https://github.com/carlok/LeanFrontier/commit/72bf82a)).
