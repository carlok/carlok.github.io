---
title: "duet: the family-labelled arm finds 164 families to the other's 64, and spends 40 % of its time paying for them"
date: 2026-11-27
tags: [math, research]
---

X12 of [duet](https://github.com/carlok/duet) ran its two arms side by side for the first time: fusion5, the parameter-disguise skip whose scale test is [X11](/blog/2026/11/26/duet-fusion5-disguise-skip-x11/), against fusion6, which adds the family label as a sixth descriptor and pushes in inverse proportion to how often the family has already been pushed, with a rescore throttle for an archive 19 times larger ([fecc0b9](https://github.com/carlok/duet/commit/fecc0b9)). Both got 28,800 s on forks of X11's 19,531-structure corpus, two searchers and two verifiers each, and the Y1–Y8 judging script was written during the block, before any family label or candidate from it existed ([b63598f](https://github.com/carlok/duet/commit/b63598f)).

Six of the eight predictions hold, and the family arm does what it was built for: at a matched 266 structured theories it reaches 132.2 families where fusion5 has 64.0, and in the runs themselves 164 against 64, with 70 new families against 4, a largest-family share of 2.7 % against 6.8 %, a higher positive share of 55.6 % against 47.5 % (Fisher p = 0.0042) and more verified theories, 734 against 560 ([notes/x12_predictions.out](https://github.com/carlok/duet/blob/main/notes/x12_predictions.out)).

Y4 and Y6 fail, and they fail in the same direction — breadth bought at the cost of depth. Its top 20 candidates carry the automatic marks less often, 3 disconnected against 8 and 4 level-7 entries against 6, and its rescores took 21,843 s of sixteen searcher-hours: 39.66 % of searcher time against a 15 % cap, with throughput at 0.65 million evaluations per searcher-hour against fusion5's 1.07 million. Both arms kept the pushes early, 99 % of them inside the first 4.1 % and 5.3 % of the block.

The run also turned up a verifier hole. Two stage-a redundancy proofs sat at z3's rlimit for 5.2 and 7.3 hours and a third ran until z3's own memory cap aborted the verifier, four times over — deviation 13, worth about 12.5 of fusion5's 16 verifier-hours. V8 now puts a wall-time cap on every z3 proof, 120 s in stages a and b and 1,800 s in c, and the capped proofs of a theory that used to hang end in seconds ([85ede91](https://github.com/carlok/duet/commit/85ede91)).
