---
title: "diaz-modulus-lean: a formalized negative result on Diaz's modulus conjecture"
date: 2026-08-21
tags: [lean4, math, project]
---

[diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean) is a new Lean 4
formalization of a negative result on Diaz's 2004 modulus conjecture: for a
candidate `u` with `e^u` and `|u|` both algebraic, the conjugate `ū` is a
rational function of `u` with algebraic coefficients, so no statement about
vanishing matrix coefficients over the algebraic hull can separate a candidate
from an ordinary complex number. It machine-checks the conjecture's question of
method — how non-holomorphic maps like conjugation and modulus could enter a
transcendence proof at all — in the negative direction.
