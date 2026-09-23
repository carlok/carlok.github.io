---
title: "LeanFrontier: nineteen submissions in a day, and what trusting a contributor would have skipped (Field Note 13)"
date: 2026-09-23
tags: [lean4, math, project]
---

[Field Note 13](https://carlok.github.io/LeanFrontier/notes/field-note-13.html) is out,
and its day was nineteen submissions — eighteen of them from the outside contributor
of the last two notes — which took the corpus from 33 to 53 modules at a speed where
the only step the contributor could not perform was the maintainer's merge click. Most
of the new work formed two clusters: the rational trees (both path enumerations of the
positive rationals, the Stern–Brocot interval invariants, and a bridge proving that a
Calkin–Wilf path and a Stern–Brocot path reach the same pair exactly when one is the
reverse of the other), and a new `Probability/` directory opened with three versions of
the Paley–Zygmund inequality plus Cantelli's and the Chung–Erdős inequality. Six of the
eleven targets in the contributor's own
[contribution directions](https://github.com/carlok/LeanFrontier/blob/main/docs/CONTRIBUTION-DIRECTIONS.md)
are now marked landed there. The last arrival sat outside both clusters: the Caro–Wei
bound, an independent set at least as large as the sum of the reciprocals of one plus
each degree, merged by hand as
[#259](https://github.com/carlok/LeanFrontier/pull/259).

That raised the narrower question the note is built around — what would a maintainer's
glance at a pull request catch that the receiver does not? Not a wrong proof; a kernel
does not accept one. It caught two things that were not about proofs at all.
[#216](https://github.com/carlok/LeanFrontier/pull/216) rejects code that runs at build
or import time (a Lean `initialize` block had passed the receiver's forbidden-construct
list, built cleanly and written a file on disk the moment another module imported it —
code execution on anyone who builds the corpus from source), and it made ordinary
submissions add-only, so a submission can no longer redefine what an accepted theorem
depends on while leaving it compiling.
[#239](https://github.com/carlok/LeanFrontier/pull/239) rejects deprecated APIs in a
submission's own files and reports them during upgrades, after
[#224](https://github.com/carlok/LeanFrontier/pull/224) replaced the thirteen
deprecations the corpus had already absorbed, and
[#241](https://github.com/carlok/LeanFrontier/pull/241) fixed conjecture probing: the
first conjecture ever submitted — a month-old claim that the coprimality assumption on
the different ideals in Mathlib's compositum discriminant identity is load-bearing —
arrived with six probe attempts where eighteen were due, because an internal list of
module names had been overwritten with declaration names, so the receiver had found no
conjecture to probe since conjectures were introduced.

Two smaller repairs rode along: the receiver now names an out-of-date branch as stale
instead of blaming it for main's changes
([#254](https://github.com/carlok/LeanFrontier/pull/254)), and its rules were recorded
as a dated pre-registration deviation
([#240](https://github.com/carlok/LeanFrontier/pull/240)). Every one of the nineteen
submissions was merged by hand, one at a time — `main` requires branches to be up to
date, so each merge left the others behind and each had to be updated and revalidated
first — and the contributor stayed off the auto-merge allowlist anyway. The manual
merge is still the cheapest place to catch misleading prose, which no receiver reads.
