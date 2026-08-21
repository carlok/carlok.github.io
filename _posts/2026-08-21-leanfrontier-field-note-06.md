---
title: "LeanFrontier: a neighbour answers half the question (Field Note 06)"
date: 2026-08-21
tags: [lean4, math, project]
---

[LeanFrontier](https://github.com/carlok/LeanFrontier)'s
[Field Note 06](https://carlok.github.io/LeanFrontier/notes/) measures the
corpus against Tau Ceti, a second machine-generated Lean 4 library, and finds
that machine mathematics does accumulate: Tau Ceti's internal import density
rose monotonically across its history, narrowing the open question to whether
accumulation survives without a human-written roadmap. The day also took the
human out of the merge path — receiver-accepted submissions now merge
themselves, and the first unattended submission opened at 15:39 and merged at
15:56:56 — and admitted conjectures as Prop-valued definitions fingerprinted
by value, so a conjecture restating known mathematics is rejected as a
duplicate. Three new submissions landed ([thue-morse-prouhet-power-sums](https://github.com/carlok/LeanFrontier/pull/142),
[stern-brocot-coprime-enumeration](https://github.com/carlok/LeanFrontier/pull/150),
[padovan-sequence-sum](https://github.com/carlok/LeanFrontier/pull/153)),
taking the corpus to 27 modules, and running the pipeline unattended surfaced
four defects that reading had missed. The measurement itself lives in the new
[lean-corpus-density](https://github.com/carlok/lean-corpus-density) repository.
