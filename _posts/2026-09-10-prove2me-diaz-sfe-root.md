---
title: "prove2me-logs: the Diaz root falls to strong four exponentials, and half the tree goes nowhere"
date: 2026-09-10
tags: [lean4, math, prove2me]
---

The Sep 9 session in [prove2me-logs](https://github.com/carlok/prove2me-logs)
closed [DiazModulus.diaz_of_sfe](https://github.com/carlok/prove2me-logs/commit/a8112aa):
with x = (1, u) and y = (1, conj u) the four products are 1, conj u, u and the
squared norm, all in the tilde space, and Hermite–Lindemann discharges from a
node the mission had already proved — so strong four exponentials is the only
hypothesis left standing. It came out of a
[design review that rejected its own design](https://github.com/carlok/prove2me-logs/commit/be95bef):
three scoped reviewers returned REJECT on the alternative route via algebraic
independence of logarithms, nothing was published from it, and the argument
turned out to already exist verbatim in the accepted `diaz_of_schanuel`
submission.

The tree was then audited rather than extended:
[recip_pi_exp_value_not_root_of_unity is Proved unconditionally](https://github.com/carlok/prove2me-logs/commit/9370755),
which fixes the shape any counterexample to the axis leaves must take — an
algebraic number on the unit circle that is not a root of unity, and those
exist, so nothing closes — and marking the interior nodes showed that
[five of the sixteen sit above exactly one leaf and are equivalent to the
root](https://github.com/carlok/prove2me-logs/commit/ac8b375), i.e. the whole
`exp_real` side, half the tree, goes nowhere. A
[port of the line exclusion](https://github.com/carlok/prove2me-logs/commit/031c39f)
from the conjugation-degree section kills the degenerate case and leaves
candidates on genuine circles, while the
[handoff note](https://github.com/carlok/prove2me-logs/commit/3703c89) records
that the hold cadence produced three contributions in one afternoon and that
two checking bugs came out of it — contributors tracked by mutable username,
and sweeps that had to be re-run.
