---
title: "179 to 172 to 200: a Stage 2 solver that improved by subtraction"
date: 2026-09-03
tags: [lean4, math, research, project]
---

[The release itself](https://carlok.github.io/) is already noted: parsimagma
[v1.0-stage2](https://github.com/carlok/parsimagma/releases/tag/v1.0-stage2)
settles all 200 problems of the SAIR Stage 2 sample set in one
standard-library-only Python file, archived at
[doi:10.5281/zenodo.22237100](https://doi.org/10.5281/zenodo.22237100) with a
write-up at [doi:10.5281/zenodo.22214743](https://doi.org/10.5281/zenodo.22214743).

This is the other half: how it got there. The score went up every time
something was taken out, and the sequence is worth writing down because the
intermediate numbers are the argument.

An early build reached **137/200** by combining my solver with the competition's
own reference solver. Embedding the Equational Theories Project's implication
graph as a bitmap, to be consulted as a truth oracle, took it to **172**. Six
strategies hardcoded to individual problem pairs — one of them literally
`if eq1_id != 719 or eq2_id != 4138: return False` — took it to **179**.

Those six were then deleted, and the score fell to **172**. That is the first
honest number of the day: the rules state the graded set reuses no publicly
available problem, so a strategy keyed to a specific pair cannot fire there. It
had been worth exactly seven points on a set it was fitted to and zero on the
one that counts.

From 172 the climb back was by general methods only. Critical-pair completion
with a proof-carrying representation reached **187**; rewriting the goal with the
derived equations, **190**. At that point the reference solver and both lookup
tables came out — and the score did not move. Everything borrowed turned out to
be reproducible locally, which is a measurement rather than a principle: 806
lines with nothing borrowed scored what 4,323 lines with a borrowed engine and
two embedded tables had scored.

Selecting the smallest derived equation instead of the oldest reached **196**.
The last four needed a real ordered superposition loop — a Knuth-Bendix ordering,
demodulation inside the loop, subsumption — which is where proofs live that
require rewrites *not* shrinking the term, and which term-size-as-a-proxy
forbids. **200/200**, confirmed by two independent runs agreeing problem for
problem, in 26 minutes, with no LLM call on any problem.

Three things I would not have predicted.

**An optimisation that prunes is a correctness change.** The isomorphism cut in
the model finder bounded a cell's value by the largest already *assigned*,
ignoring that the cell's own row and column are elements it mentions. It looked
obviously sound. Audited against an exhaustive oracle over 595 problem/size
pairs, it silently lost three real counterexamples.

**Proof compression is a feasibility threshold, not a nicety.** One proof
flattens to 3,634,949 bytes against a 100,000-byte cap. Emitted from the
inference DAG — each derived lemma stated once as a `have` and cited — it is
13,728. The same proof is submittable or not depending only on how it is written
out.

**Replay is not verification.** Confirming a rewrite path reaches the intended
term does not confirm each rewrite was *applicable* where it claims. A path can
arrive correctly and contain a step that means nothing. Where the harness gives
no verifier in the loop, that check has to be explicit.

The proofs of true implications close over no Lean axioms at all — `#print
axioms` returns the empty list rather than the three the judge permits. On the
challenge Zulip, [Alex
Meiburg](https://zulip.sair.foundation/#narrow/channel/13-Math-Distillation-Challenge---equational-theories)
pointed out this is expected rather than surprising, and Juan Padilla corrected
the attribution from Gödel to **Birkhoff**: an equation holding in every model of
an equational theory has a derivation by substitution and replacement alone, so
no axioms are needed. The existence is a theorem. What the solver does is
produce one mechanically for every true implication in the set, inside the size
cap, without searching for axiom-freeness as a separate goal. The write-up now
cites Birkhoff and says so; the correction is in the version history rather than
quietly swapped in.

Everything is Apache-2.0 and public — solver, the prover as separate readable
modules, per-problem results, every measurement — at
[carlok/parsimagma](https://github.com/carlok/parsimagma). It went up hours
after the deadline rather than at it, because two other entrants asked for that.

Written by AI agents under my direction: two models, given the same brief and no
contact with each other, both closed the two hardest problems independently,
which is the main reason I believe those two. Every figure here was measured by
my own tooling rather than reported by the models that wrote the code.
