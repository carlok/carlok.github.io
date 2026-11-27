---
title: "duet: moving the disguise skip into the search takes it from 294 of 578 verified theories to none of 640"
date: 2026-11-26
tags: [math, research]
---

X11 of [duet](https://github.com/carlok/duet) put the parameter-disguise screen into the search itself. `soup.paramskip` checks 5,008 linear parameter terms — x and y once, z·z or z∘z, two to four operations — against the corpus models in a numba kernel at each cell win, confirms the survivors with Mace4 on two to five elements and keeps the countermodels; replayed over X6 to X10 it would have skipped all 711 theories V6 had marked as disguises, no level-7 or level-8 theory, and 34 it would have got wrong, which E then refutes ([70ba826](https://github.com/carlok/duet/commit/70ba826)).

The run was preregistered before it started — eight hours in blocks, four searchers and four verifiers as in x10b, seeds 1601+, seven predictions — and all seven held in a single block that spent 28,834 s to budget with no memory stop, the closest call 1,050 MB available ([695a31b](https://github.com/carlok/duet/commit/695a31b), [3bb3818](https://github.com/carlok/duet/commit/3bb3818)). Not one of the 640 verified theories is a parameter disguise, against 294 of 578 in X10, and the screen cost 0.11 % of searcher time; 30.57 million evaluations over 32.02 searcher-hours is 0.95 million per hour against a 0.75 million bar. Structured theories went from 11.0 % of X10 to 48.0 %, with 16 new families out of 60 and a Chao1 index of 204 over the 170 families found so far.

The candidates moved with them: 5 of 20 have a classical model where X10 had 15, 10 of 20 are disconnected where X10 had 4, and `1f430506` and `1238c063` take the top two N1 ranks unstudied ([notes/x11_predictions.out](https://github.com/carlok/duet/blob/main/notes/x11_predictions.out)). What the run also exposed is a queue problem, post hoc and not preregistered: the push gate stalls the search once verified scores rise, and 99 % of X11's 3,291 pushes came in the first 805 s, against 9.9 % and 34.7 % of their blocks in x10b and x8b.
