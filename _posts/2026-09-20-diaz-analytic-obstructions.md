---
title: "diaz-modulus-lean and prove2me-logs: the two analytic obstructions fall, and the library says the 1973-74 theorem is proved"
date: 2026-09-20
tags: [lean4, math, research]
---

The two items [diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean)
still listed under "What is not proved" — real analysis and interpolation
determinants, it said — are proved, and neither needed them
([2bc0828](https://github.com/carlok/diaz-modulus-lean/commit/2bc0828)).
`DiazModulus.no_first_order_arithmetic_operator` shows why Schneider–Lang has no
input here: for a candidate `u` and `F(z,w) = exp(uz + conj u w)`, a first-order
operator `a ∂/∂z + b ∂/∂w` with polynomial coefficients whose values on `Z²` are
all algebraic must have `a = b = 0`, because the bracket `a(m,n)u + b(m,n)conj u`
is algebraic — the exponential factor is a non-zero algebraic number — Baker
(carried as an explicit hypothesis, since Mathlib has no form of it) kills it, and
a polynomial vanishing on a product of infinite sets is zero; `∂/∂z ∂/∂w`, by
contrast, does take algebraic values and is not a derivation.
`DiazModulus.kronecker_factorisation` closes the second: the matrix of values of
`exp(auz + b conj u w)` on the lattice is the Kronecker product of two Vandermonde
matrices, so its determinant is a product of powers of theirs and is non-zero —
the nodes are distinct because `|exp u| = exp(Re u) ≠ 1`, and the candidate's
arithmetic does not appear in it. Both hypothesis classes are conjecturally empty,
which the nodes say on their face, and neither claims novelty; the first is stated
for polynomial coefficients where the note states it for rational functions
regular on `Z²`, since clearing denominators is not formalised. The library now
holds [166 of 166 proved
nodes](https://github.com/carlok/diaz-modulus-lean/blob/master/MIRROR_CHECKLIST.md),
axioms clean, and the dead-branch table for the four superseded `FourExp`
statements moved into `refresh_prove2me_archive.py`, because the file carrying it
is generated and the refresh had been overwriting it.

Those four statements are the subject of the day's second commit
([8a80cc0](https://github.com/carlok/diaz-modulus-lean/commit/8a80cc0)): they stay
Open on the platform and stay in `archive/prove2me/open/` because two accepted
reductions import them, but none of them will ever be proved — two fix the wrong
`S`, two omit the hypothesis that the four exponentials are algebraic — so each
node's `Source` line now names its corrected replacement and the defect, and the
archive's `open/README.md` carries the same table. The two citing reductions, the first sketches of `auxiliary_construction`
and `construction_core_1973`, were accepted before the defects were found; both
nodes are Proved through their second sketches. The third commit is the
documentation catching up with the mathematics
([f8d2ce5](https://github.com/carlok/diaz-modulus-lean/commit/f8d2ce5)): the note
and the README predated the four exponentials work and contradicted it, with the
abstract and section 5 saying the transcendence-degree-one case had never been
formalised and naming Philippon's zero estimate as the obstacle, and the appendix
row reading Open. All three were wrong, and the second was wrong about the route
as well — Waldschmidt's own 1973 proof, with the toolbox of his 1971 paper, uses
no zero estimate and no Baker. Both places are rewritten, the appendix row reads
Proved, the 1971 paper is cited and the PDF rebuilt; the README gains a section on
the subtree (the statement as the node gives it, the modules it consists of, and
the two statements about `1/π` that still block the branch), and
`formalization.yaml`, which still listed two axioms and said in three places that
the wider development depends on them, now says the project assumes nothing beyond
Lean's three axioms.

The journal in [prove2me-logs](https://github.com/carlok/prove2me-logs) records
both obstructions with the mission entry they closed
([a93858e](https://github.com/carlok/prove2me-logs/commit/a93858e), the entry
itself is
[missions/diaz/2026-09-19-the-two-obstructions.md](https://github.com/carlok/prove2me-logs/blob/main/missions/diaz/2026-09-19-the-two-obstructions.md)):
the reading queue is now empty and what is left under the root is three open
research problems. `HANDOFF.md` had still been telling whoever picked the mission
up *not* to attempt the four exponentials theorem, Philippon's zero estimate named
as the blocker, and it is replaced by what is actually there
([49d4149](https://github.com/carlok/prove2me-logs/commit/49d4149)) — three open
leaves, all open mathematics, each implied by strong four exponentials and none of
them a formalisation task: the two halves of `1/π` not being an algebraic multiple
of a purely imaginary logarithm, and another contributor's node equivalent to the
whole root.
