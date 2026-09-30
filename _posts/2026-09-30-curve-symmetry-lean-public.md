---
title: "curve-symmetry-lean is public: the note and its Lean port"
date: 2026-09-30
tags: [lean4, math, project]
---

[curve-symmetry-lean](https://github.com/carlok/curve-symmetry-lean) went public
on 30 September: the note *Sharp symmetry bounds for real algebraic curves*, as
[PDF and TeX](https://github.com/carlok/curve-symmetry-lean/blob/main/sharp_symmetry_bounds.tex),
together with the Lean 4 port that checks every theorem, lemma and remark of it
— 108 modules and about 900 theorems and lemmas, using only `propext`,
`Classical.choice` and `Quot.sound`, with no `sorry` and no `native_decide`
([f0b97b7](https://github.com/carlok/curve-symmetry-lean/commit/f0b97b7)).
[COVERAGE.md](https://github.com/carlok/curve-symmetry-lean/blob/main/COVERAGE.md)
maps each claim to its declarations and to the reading it is checked at: for
`d >= 5` the note classifies the curves attaining the maximum `max(d, 2d-4)`
rotations as `Re(z^(d-2)(|z|^2 + a)) = 0` up to similarity, with their exact
ambient Möbius groups, and the port reaches the genus from an explicit basis of
holomorphic differentials rather than Riemann–Hurwitz. Theorem 1 alone is also
published in
[sharp-symmetry-bounds-lean](https://github.com/carlok/sharp-symmetry-bounds-lean)
and registered with Palomar as `PALOMAR-2026-09-18-000007`. The last sprints
before publication put the machine-checked halves into the prose — an
[Appendix A to the note](https://github.com/carlok/curve-symmetry-lean/commit/f618c4a)
saying where each statement is checked, by what, and who checked it — and added
[negative controls](https://github.com/carlok/curve-symmetry-lean/commit/35f51bc)
that make three mutated copies of the registry entry fail their own pre-checks
for the intended reason. An e-mail to Alcázar, Lávička and Vršek went out on 30
September reporting that the note's irreducible quintic is a counterexample to
Lemma 9 of their
[arXiv:1801.09962v1](https://arxiv.org/abs/1801.09962v1); no novelty is claimed
anywhere, and
[CHECKS.md](https://github.com/carlok/curve-symmetry-lean/blob/main/CHECKS.md)
records exactly what has and has not been checked.
