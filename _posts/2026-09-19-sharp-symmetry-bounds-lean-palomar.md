---
title: "sharp-symmetry-bounds-lean registered in the Palomar registry: PALOMAR-2026-09-18-000007"
date: 2026-09-19
tags: [lean4, math, project]
---

[carlok/sharp-symmetry-bounds-lean](https://github.com/carlok/sharp-symmetry-bounds-lean)
is now a registered entry in the Palomar registry —
[PALOMAR-2026-09-18-000007, version 1](https://palomar-registry.org/entry?id=PALOMAR-2026-09-18-000007&version=1),
status `registered`, trust level `high`, on the source of
[commit `ced9fe2`](https://github.com/carlok/sharp-symmetry-bounds-lean/commit/ced9fe2d4d2aa42aa03bbc19b1b56cdcd18c9413)
(the record's own copy of the entry is
[here](https://data.palomar-registry.org/entries/PALOMAR-2026-09-18-000007-v1.json)).
This is the first third-party verification of one of these formalizations, and
what the registry actually did is the news: it rebuilt the project in a sandbox
from the pinned dependencies (Lean v4.32.0), exported the proof terms with
`lean4export` and replayed them on **nanoda**, an independent kernel
implementation rather than the author's own build, then used the
[Comparator](https://github.com/PalomarRegistry/PalomarSubmission/actions/runs/35351732435)
to check that `Solution.lean` proves the `Challenge.lean` statements — five
theorems of `SharpSymmetryBounds` — using only `propext`, `Quot.sound` and
`Classical.choice`, verified at 2026-09-18T13:50:47Z.

An immutable copy of the source was then archived with a receipt hash
(2026-09-18T14:30:13Z): carlok/sharp-symmetry-bounds-lean was forked by
[PalomarArchive](https://github.com/PalomarArchive/carlok--sharp-symmetry-bounds-lean--f3036be09495),
the registry's archive organisation, at the same `ced9fe2` commit. Automated
editorial review came back `neutral` with no warnings, and the machine-readable
evidence — build, replay, comparison, axioms — is published alongside the entry.
The record certifies that the Lean proofs check, not that the result is new.
The repository's own commits the same day are this story:
[the working note recorded as the formalized source](https://github.com/carlok/sharp-symmetry-bounds-lean/commit/ced9fe2),
[the registry record linked from the README](https://github.com/carlok/sharp-symmetry-bounds-lean/commit/c31d363)
and [citation metadata and badges](https://github.com/carlok/sharp-symmetry-bounds-lean/commit/5cc8c57).
