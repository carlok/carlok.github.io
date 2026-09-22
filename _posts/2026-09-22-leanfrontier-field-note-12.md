---
title: "LeanFrontier: the stranger came back, and their harness found the receiver's bug (Field Note 12)"
date: 2026-09-22
tags: [lean4, math, project]
---

[Field Note 12](https://carlok.github.io/LeanFrontier/notes/field-note-12.html) is
out, and its subject is the contributor from Field Note 11 — the account behind
[the fork covered earlier this month](/blog/2026/09/12/leanfrontier-fork-qazw12345/) —
returning with two theorems built on modules already in the corpus rather than two
isolated results. [#179](https://github.com/carlok/LeanFrontier/pull/179) proves
the local descent step of the Markov tree: for an ordered positive Markov triple
other than `(1,1,1)`, the Vieta jump in the largest coordinate is positive, at most
the middle coordinate and so strictly smaller than the largest.
[#180](https://github.com/carlok/LeanFrontier/pull/180) bridges the accepted
Ford-circle criterion to Mathlib's own geometry: two Ford circles with non-zero
denominators are externally tangent in the sense of
`EuclideanGeometry.Sphere.IsExtTangent` exactly when their cross determinant
squares to one. The receiver accepted them in 111 and 79 seconds, with zero exact
Mathlib matches, kernel replay, downstream import and all 118 and 119 entrypoints
already in the corpus still passing.

The more useful find was theirs about the receiver. Their agent runs a plain
`lake build` before submitting, because the receiver only ever answered
`BUILD_FAILED` — and that turned out to be a defect rather than a design choice.
Lake prints the Lean errors on standard output and only the summary line on
standard error, and the receiver kept standard error, so every build rejection
reported one sentence with no error in it; [#187](https://github.com/carlok/LeanFrontier/pull/187)
keeps both streams, and [#193](https://github.com/carlok/LeanFrontier/pull/193)
narrows that to the submitter's own file rather than the tail of the build.
Admission rules did not change, only the text of a rejection.

The day's other work is the weekly Mathlib v4.34.0 upgrade, which took three runs
([#188](https://github.com/carlok/LeanFrontier/pull/188)): Mathlib's download cache
had no compiled file for `Mathlib.Probability.Kernel.Invariance`, `cache get`
reports such gaps as a warning and exits successfully, and the index build then
failed on the missing module, so [#185](https://github.com/carlok/LeanFrontier/pull/185)
now builds whatever the download left out. The second run built everything but was
refused for carrying evidence older than a moved `main`; the third gave the audit
jobs more time ([#189](https://github.com/carlok/LeanFrontier/pull/189)) and stopped
auditing each head twice ([#190](https://github.com/carlok/LeanFrontier/pull/190)).
The corpus built unchanged on the new release, all 120 entrypoints passed the
kernel recheck, and none was an exact duplicate of anything new in Mathlib. Merged
since: [#201](https://github.com/carlok/LeanFrontier/pull/201) kills a timed-out
command's whole process group instead of the command, [#204](https://github.com/carlok/LeanFrontier/pull/204)
reads generated-PR staleness from git rather than `mergeStateStatus`, and
[#200](https://github.com/carlok/LeanFrontier/pull/200) writes down the
contribution directions and PR cadence — the answer to the contributor's question
about what should slow an agent down, which is mechanical cost rather than a rule.
