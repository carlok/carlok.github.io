---
title: "moebius-transcendental-lean v0.2.0: the conjugation-degree spectrum is classified"
date: 2026-09-02
tags: [lean4, math, research]
---

[moebius-transcendental-lean](https://github.com/carlok/moebius-transcendental-lean)
tagged [v0.2.0](https://github.com/carlok/moebius-transcendental-lean/releases/tag/v0.2.0),
which classifies the conjugation-degree spectrum on the transcendental locus:
`conjDegree` attains every value in ℕ∞ except 0, which it never attains. Every
finite degree gets the same explicit witness, zₙ = sⁿ + i·s with
s = liouvilleNumber 2, while the ⊤ stratum comes from an algebraically
independent real pair. It compiles against Mathlib v4.32.0 with no `sorry`,
and the permanent axiom-verification module confirms the ten new declarations
close over exactly `{propext, Classical.choice, Quot.sound}`.
