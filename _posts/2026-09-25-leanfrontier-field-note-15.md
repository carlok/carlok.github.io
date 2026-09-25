---
title: "LeanFrontier: seven modules deep, and a five-week-old semiconjugacy finished (Field Note 15)"
date: 2026-09-25
tags: [lean4, math, project]
---

[Field Note 15](https://carlok.github.io/LeanFrontier/notes/field-note-15.html) is
out, and both submissions of its day were merged without anyone touching a
button. [#307](https://github.com/carlok/LeanFrontier/pull/307) shows that the
three oriented Markov branches the coverage theorem split out are one branch up
to a cyclic permutation of the coordinates, and packages the permutation that
carries the canonical branch onto each of the others — which puts the module at
the end of the corpus's deepest chain: Markov equation, descent step, path
layer, orientation, Stern–Brocot bridge, coverage, symmetry, seven modules and
six import hops, all six built since Monday.
[#308](https://github.com/carlok/LeanFrontier/pull/308) finishes a result left
five weeks earlier: the Ulam–von Neumann semiconjugacy between the tent map and
the logistic map at parameter four, submitted on 18 August through the change of
variables `x ↦ sin (π x / 2)²`, was missing the structural fact that that change
of variables is a homeomorphism on the unit interval, so supplying it upgrades
the semiconjugacy to a topological conjugacy — the two maps are the same
dynamical system seen through a change of coordinates.

Both came through the [maintainer merge
queue](/blog/2026/09/24/leanfrontier-docs-proposals-merge-queue/) added the day
before, including its one untested path: bringing a fork's branch up to date
with the project's automation token rather than a maintainer's credentials,
relying only on the contributor having allowed edits by maintainers. It worked
twice, and the second submission needed it — it fell behind by three commits
when the first merged and by five more when the automated follow-ups landed, so
the queue updated it, waited for the whole receiver to run again, and merged it.
The corpus is at 65 modules and 45 internal import edges, 0.69 per module,
against the 0.17 recorded when the suspended experiment was registered.
