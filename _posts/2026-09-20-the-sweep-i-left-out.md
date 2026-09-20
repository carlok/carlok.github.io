---
title: "200 to 181: the sweep I had already written and left out"
date: 2026-09-20
tags: [lean4, math, research]
---

The graded results for the SAIR Stage 2 challenge are in. My solver scored 181
of 200, the same figure on both tracks from the same file. Earlier I wrote
about how it reached 200 on the organizer's published sample set by removing
things: six per-problem gates, a borrowed reference solver, two lookup tables.
That post was right about what it described and incomplete about what it
implied.

All nineteen missing points sit in one category, and all nineteen carry judge
status `not attempted`. The solver emitted no incorrect certificate on two
hundred private problems, which is the property I designed for. It is also why
the failure was invisible. Nothing in the output says "there is a countermodel
at carrier 8 and you did not look."

Because there is. Seven of the nineteen have one. My search ran carriers 2
through 7. My certificate emitter carried this line, with the comment already
written:

    TABLE_MAX_CARRIER = 10          # finOpTable reads one character per entry

Adding `8` to one tuple finds all seven, in 3.2 seconds of compute against a
budget of 3,600 seconds per problem. Two magmas cover all seven. The searching
half and the emitting half of the same program disagreed about how far to go,
and no test caught it, because no test exercised both halves at once.

Ten more fall to linear magmas over Z/7 and Z/11, found by solving for
coefficients in milliseconds. That code is in the repository. It was published
separately on the Contributor Network. It was not in the file I submitted,
which contains no family search of any kind. Five of those ten sit at carrier
7, inside the range I did search; brute-force table search failed on all five
at 300 seconds each, where the coefficient check returns them at once.

So here is the correction to the earlier post. Removing per-problem gates was
right, because a gate keyed to a problem id is a stored answer. Removing
construction families was a different act, and I treated it as the same one. A
generator that a search ranges over is a mechanism, and mechanisms are the part
you keep.

Two smaller things I would not have predicted. The cheapest bug in the whole
run was a constant, not an algorithm. And a solver that never guesses fails
quietly: soundness and silence are the same behaviour seen from two sides, and
only one of them shows up in the logs.

Five of the ten would have needed one more fix even so. `finOpTable` reads the
table one digit per character, so any model with an element numbered 10 or
above is silently corrupted. The obvious workaround is blocked as well: the
judge admits declarations by prefix, and of its 59 allowed prefixes `Fin.`,
`Nat.` and `OfNat.` are there while `HAdd.` and `HMul.` are not. So
`a * x + b * y` is rejected, and the same function written through `Fin.add`
and `Fin.mul` is accepted. Both facts sit in the judge's own published source,
which is where I would have found them if I had gone looking.

I used 1.43% of the wall clock I was allowed. The failures do not yield to
fifteen times more of it. It was never a question of compute.

The full post-mortem, with what was run and what it returned for every figure,
is at
[docs/stage2-result.md](https://github.com/carlok/parsimagma/blob/main/docs/stage2-result.md).
Computation and drafting were done with AI assistance under my direction; every
number here was recomputed by my own tooling.
