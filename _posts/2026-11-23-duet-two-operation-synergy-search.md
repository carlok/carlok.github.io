---
title: "duet: an open search over two-operation theories, and a funnel built to tell rediscovery from novelty"
date: 2026-11-23
tags: [math, research]
---

[duet](https://github.com/carlok/duet) is a new repository, public since 21 November, asking whether a machine can find unpicked fusions in algebra: small theories in two binary operations · and ∘ with a law that the theory implies but no single one of its laws does. A lattice is the named example — two absorption laws force `x · x = x`, neither alone — and duet searches the space of 1–6-law sets, which is 1.84 × 10²⁶ of them, with a MAP-Elites search over 71,369 laws and streaming verification by E, Vampire, Mace4 and Lean. No language model sits in the scoring loop.

The repository's discipline is the funnel, regenerated after each run by `notes/funnel.py` ([3ae577a](https://github.com/carlok/duet/commit/3ae577a)): 53,303,636 cheap evaluations against 12,509 small structures, 5,279 verified through the provers and finite-model search, 4,714 with a proved emergent law, 3,431 that are not a fragment of a lattice, quasigroup, skew lattice or other named theory, 158 candidates, 125 distinct varieties, 82 that no check recognises, 22 bearing every automatic mark, and 2 studied closely and still unidentified. Level 0 covers 2.9 × 10⁻¹⁷ % of the space and is an upper bound, since a theory seen twice counts twice.

Run X5 finished at 00:10 UTC on 23 November with all three preregistered predictions intact: of 164 scored theories none implies an argument-ignoring law, none reproduces X4's top-ten laws, and the square-claim share comes in at 73 % against 85 % ([b0359c7](https://github.com/carlok/duet/commit/b0359c7)). The after-run reading is the interesting part — X5's 20 candidates merge into 5 varieties across runs, and 16 of the 20 are Steiner loops whose ∘ is · translated by a constant, a disguise the fragment filter does not catch ([4af0a8f](https://github.com/carlok/duet/commit/4af0a8f)). T6 attacked S12 ⇒ `x · x = x ∘ x` with four provers at 7,200 s each: no proof, no finite countermodel on six elements or fewer, size 7 still in SAT solving — still open ([cbe0f0f](https://github.com/carlok/duet/commit/cbe0f0f)).

Nothing here is claimed to be new. `REPORT.md` carries every number with the command that produced it, and the README says plainly that a literature search is weak evidence and that the search grows like coral, outward from known mathematics.
