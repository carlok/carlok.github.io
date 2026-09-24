---
title: "diaz-modulus-lean: the companion note reaches 1.3, and the mirror closes at 200 of 200"
date: 2026-09-24
tags: [lean4, math, research]
---

Three versions of the companion note to [diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean)
landed in twenty-four hours, and the mirrored library grew with each: 182 of 182
proved results at [note-v1.1](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.1),
195 of 195 at [note-v1.2](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.2),
and [200 of 200 at note-v1.3](https://github.com/carlok/diaz-modulus-lean/commit/ac58474),
with `lake build Diaz` clean and nothing behind the headline theorems but `propext`,
`Classical.choice` and `Quot.sound`.

[Version 1.1](https://github.com/carlok/diaz-modulus-lean/commit/21fe1ec) takes the
boundary from three open statements to two: version 1.0 had listed the real half of
(S), its imaginary half and the transcendence of `|u|`, but both branches that reach
(S) produce a real γ, so the imaginary half is not needed — and by Gelfond–Schneider
the exceptions to (S) lie on at most one rational line, on an axis, so the two halves
cannot both fail. [Version 1.2](https://github.com/carlok/diaz-modulus-lean/commit/c21b03f)
gives the smallest open instance a partner: at least one of `√((log 2)² + π²)` and
`2^{i log 2/π}` is transcendental, the arguments of the candidates on a circle of
algebraic radius form a Sidon set up to conjugation, and `(−1)^{u/ū}` is transcendental
for every candidate. [Version 1.3](https://github.com/carlok/diaz-modulus-lean/commit/db91437)
turns the closing remark into a theorem — on the data a candidate certifies, `u`, `ū`
and `iπ`, every singular 2×2 matrix of rational combinations has ℚ-dependent rows or
columns, so the four exponentials conjecture is already a theorem there — sharpens what
separates the strong form from the ordinary one to the constant term rather than the
algebraic coefficients, and corrects 1.2's claim that `r·e^i` is "certainly not" a
candidate.

Each release says the same thing about novelty and the note repeats it: every result is
elementary, or a short consequence of Gelfond–Schneider, of the six exponentials theorem,
or of the four exponentials theorem in transcendence degree one — what is new is that the
chain is machine-checked, with Appendix A identifiers re-checked against the platform by
script at zero mismatches. The journal in
[prove2me-logs](https://github.com/carlok/prove2me-logs/commit/ba8cd7b) records the same
five steps, from [Gelfond–Schneider closing the classical theorems](https://github.com/carlok/prove2me-logs/commit/07a3293)
to [the four-exponentials barrier](https://github.com/carlok/prove2me-logs/commit/ba8cd7b).
