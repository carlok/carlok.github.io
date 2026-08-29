---
title: "parsimagma-greedy-cover: a refuter published on the SAIR Contributor Network"
date: 2026-08-29
tags: [math, tool, contribution]
---

[parsimagma-greedy-cover](https://competition.sair.foundation/contributor-network/mathematics-distillation-challenge-equational-theories-stage2/EQT02-S00025)
is now public on the SAIR Contributor Network, entered into the Mathematics
Distillation Challenge Stage 2. It is a deterministic refuter with no LLM calls:
given two equational laws it finds a finite magma satisfying the first and
violating the second, and emits a Lean 4 certificate the organisers' judge
accepts under plain `decide`. The point of publishing is the ordering rather
than the score — four instances of `Z/2` refute 11,871,871 of the ETP's
13,855,357 false implications, twenty-five refute 97.2%, and `x ◇ y = 7x + 7y`
over `Z/13` alone refutes 268 pairs that Vampire's `fmb`, Mace4 and z3 on a
ground encoding all fail to find. The honest number is on the item: 55 of 200 on
the graded distribution, zero on the true half by design, and zero on the
`extra_hard` category, which is selected against exactly this method.
