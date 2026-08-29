---
title: "parsimagma: a coverage engine over the Equational Theories Project law set"
date: 2026-08-29
tags: [math, tool, research]
---

[parsimagma](https://github.com/carlok/parsimagma) is a new public signature and
coverage engine over the 4,694 equational laws of the
[Equational Theories Project](https://teorth.github.io/equational_theories/),
asking which ETP constructions cover which separations. Its central finding is
that the residual is not uniformly hard: at least 411 of the 1,062
Vampire-unresolved implications have finite countermodels on 9 to 32 elements,
found in seconds by a structured algebraic sweep where three SAT/SMT-style
solvers all fail from carrier 11 upward. The repo also argues the published
count of unresolved implications sits below a provable floor and independently
reproduces corrected figures for the paper's section 5.1.
