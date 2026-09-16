---
title: "prove2me-logs: the zero count closes, and Gel'fond's criterion with it"
date: 2026-09-15
tags: [lean4, math, prove2me]
---

The Sep 15 entries in [prove2me-logs](https://github.com/carlok/prove2me-logs)
pick the Diaz mission up where the previous posting left it — the zero count
split, with a hole in its source — and carry it to the end of the branch. Every
FourExp leaf was given a reduction rather than a citation
([e14a87b](https://github.com/carlok/prove2me-logs/commit/e14a87b)), the
transcendence criterion was written out as a Lean argument
([75ed372](https://github.com/carlok/prove2me-logs/commit/75ed372)), and two of
the classical leaves were proved from what Mathlib already has: Gel'fond's
height bound for a divisor, which is the Mahler-measure file plus the last
inequality, and the resultant step that Mathlib reaches through the Bézout
identity but has to finish with the Leibniz expansion instead of Hadamard
([bed556a](https://github.com/carlok/prove2me-logs/commit/bed556a)).

The remaining zeros in the count then closed in order: the Cauchy estimate with
zeros ([7914918](https://github.com/carlok/prove2me-logs/commit/7914918)), the
radius choice itself ([634590c](https://github.com/carlok/prove2me-logs/commit/634590c)),
and the count ([6f39126](https://github.com/carlok/prove2me-logs/commit/6f39126))
— after which Gel'fond's lemma, the last open lemma under the criterion, was
proved and the criterion with it
([8abaa43](https://github.com/carlok/prove2me-logs/commit/8abaa43)), leaving
the 1973 construction as the branch's remaining frontier. The entries carry the
statements, the platform node each one closed, and — as the journal's format
requires — what is not proved nearly as loudly as what is.
