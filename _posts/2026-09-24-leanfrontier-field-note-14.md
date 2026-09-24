---
title: "LeanFrontier: nine submissions, every one built on something the corpus already accepted (Field Note 14)"
date: 2026-09-24
tags: [lean4, math, project]
---

[Field Note 14](https://carlok.github.io/LeanFrontier/notes/field-note-14.html) is out, and
its day is nine submissions that each import an accepted result rather than starting beside
it: most build on results accepted the day before, one on a module accepted three hours
earlier, and one on the Furstenberg topology another contributor landed on 18 August — so
the note's own answer does not need a second producer, only an accepted one. The named
work includes explicit Thue–Morse cube sums via Prouhet and Nicomachus, the Markov tree
path layer that makes the descent step iterable, the classical Turán bound derived from
the Caro–Wei bound accepted the previous evening, the Horadam addition formula built on the
companion matrix, Sylvester's reciprocal series summed to infinity, and Markov root
reachability — every positive Markov triple reached from `(1,1,1)` by Vieta moves, the
third of three consecutive mornings whose results each became the next one's substrate.

The corpus is at 62 modules, and the reuse it measures crosses producers: 22 of its
internal import edges have a source and a target contributed by different people, so
cross-producer reuse is the normal case rather than a first. The note is careful about what
that proves — nine consecutive importing submissions are the shape of an answer to the
pre-registered question of whether machine mathematics accumulates, not yet the measurement
— and it notes the way the add-only rule from
[Field Note 13](/blog/2026/09/23/leanfrontier-field-note-13/) makes an import edge the only
way to extend accepted work, which the analysis will have to discount rather than celebrate.
Nothing was rejected: each submission was merged in turn, its branch updated and revalidated
against the corpus it would join, which is where a collision between two same-morning
modules would have surfaced. The deepest chain now runs five modules and four import hops —
Markov equation, descent step, path layer, orientation, and the bridge that aligns the
oriented Markov tree with the Stern–Brocot recursion — and the last two arrived an hour
apart.
