---
title: "quadratula: how much of Schröder's 990 quasigroup laws small quasigroups already witness"
date: 2026-09-13
tags: [math, research, rust]
---

[quadratula](https://github.com/carlok/quadratula) is a new public repository that
asks how much of the implication structure of Schröder's 990 quasigroup equational
laws is already visible in small quasigroups. It enumerates every quasigroup of order
1 to 6 up to isomorphism — 1,131,984 classes, in Rust on a pinned toolchain — computes
which laws each one satisfies, and measures that exhaustive floor against Bruno
Le Floch's [arXiv:2603.29909](https://arxiv.org/abs/2603.29909): quasigroups of order
at most 4 already witness 95.34% of the 726,207 law-level non-implications (91.68% of
the 1,958 between the 47 classes), and going to order 6 reaches 96.70%, realising 94 of
the 114 varieties and separating 42 of the 47 classes.

The floor does not finish the job, and because it is exhaustive that is a statement
about the mathematics rather than about the search: 94 class-level non-implications
still have no witness below order 7, so any finite counterexample to them has order at
least 7. A cover of 17 quasigroups — proven optimal by ILP, against 20 for a greedy
cover — witnesses everything the floor witnesses, and
[REPORT.md](https://github.com/carlok/quadratula/blob/main/REPORT.md) and
[CONTROLS.md](https://github.com/carlok/quadratula/blob/main/CONTROLS.md) are generated
with no hand-typed numbers, with the claims re-checked independently by a separate
parser and evaluator, Le Floch's raw files, and kissat. The sections past the divider
extend the exact results to orders 7–9, and nothing is certified in Lean yet.
