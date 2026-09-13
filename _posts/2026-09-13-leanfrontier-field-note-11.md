---
title: "LeanFrontier: a stranger ran the same machine (Field Note 11)"
date: 2026-09-13
tags: [lean4, math, project]
---

[Field Note 11](https://carlok.github.io/LeanFrontier/notes/field-note-11.html)
— "A Stranger Ran the Same Machine" — records the corpus's first contribution
from a first-time outside author: [qazW12345](https://github.com/qazW12345),
whose [fork was the previous day's news](/blog/2026/09/12/leanfrontier-fork-qazw12345/),
sent [PR #175](https://github.com/carlok/LeanFrontier/pull/175) formalizing
Nesbitt's inequality, `3/2 ≤ a/(b+c) + b/(c+a) + c/(a+b)`, by clearing a
positive common denominator onto
`2N - 3D = (a-b)²(a+b) + (b-c)²(b+c) + (c-a)²(c+a)`. The only human
intervention was approving the paused first-time-fork workflow; the trusted
receiver then accepted the submission in 107 seconds — 61 added lines, no exact
Mathlib fingerprint match, a kernel replay pass and an allowed axiom closure of
`propext`, `Classical.choice` and `Quot.sound` — and the theorem is now
importable as `LeanFrontier.Analysis.Nesbitt`, with the report and observation
persisted by the usual generated changes
([PR #178](https://github.com/carlok/LeanFrontier/pull/178)). Nobody judged the
proof's elegance or importance, which is the point: an unfamiliar contributor
reached the same boundary through the ordinary public route. The corpus is at
[carlok.github.io/LeanFrontier](https://carlok.github.io/LeanFrontier/).
