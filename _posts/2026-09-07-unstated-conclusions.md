---
title: "unstated-conclusions: theorems whose proofs deliver more than they state"
date: 2026-09-07
tags: [lean4, math, research]
---

[unstated-conclusions](https://github.com/carlok/unstated-conclusions) (public
since Sep 6) is the dual of
[unused-assumptions](https://github.com/carlok/unused-assumptions): instead of
weakening hypotheses, it asks which theorems in Mathlib prove a *stronger
conclusion* than they state. It reads the root of the proof term — if the last
step is a weakening lemma (`le_of_lt`, `Or.inl`, `Exists.intro w _`,
`And.left`, …), the stronger statement is already there as a subterm with its
own proof, so the finding typechecks by construction. A hand-written table of
22 weakening lemmas is the only judgement. The project runs in two parts with a
statistical wall between them: Part 1 is a pilot at the fifty-candidate gate on
unused-assumptions' own survivors (a rate there is a rate among those theorems,
and nothing more), and Part 2, the library-wide measurement, starts only after
Part 1's table is frozen.
