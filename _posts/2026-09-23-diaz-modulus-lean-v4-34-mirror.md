---
title: "diaz-modulus-lean: thirteen warnings the v4.34 bump left in the mirror, and a header that now says what changed"
date: 2026-09-23
tags: [lean4, math, research]
---

The Lean and Mathlib v4.34.0 bump in [diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean)
([a4f0779](https://github.com/carlok/diaz-modulus-lean/commit/a4f0779), the same
weekly bump that moved the rest of the Lean portfolio, most of it written up
[on 21 September](/blog/2026/09/21/mathlib-v4-34-0-portfolio/))
left thirteen warnings behind, all of them in ported mirror modules: eleven tactic
steps the unused-tactic linter now reports as doing nothing — four `push_cast`, five
`field_simp <;> ring` whose `ring` never runs, a `gcongr <;> positivity` — and two
`haveI` the linter asks to be `have`. Each is removed or respelled
([0c7ef1b](https://github.com/carlok/diaz-modulus-lean/commit/0c7ef1b)), and because the
edits also live in the porter's patch table, regenerating the mirror reproduces them
instead of reintroducing them: the porter's `--verify` reads 117 identical and 0
differing against this commit.

Nineteen ported modules differ from their archived platform submissions by library
names and spellings that changed between the platform's Mathlib (v4.33.1) and v4.34.0 —
`if_pos`/`if_neg`, `prod_le_prod`, `house_pow` becoming an equality, and
`MvPolynomial.coeff d p` spelled as `p.coeff d`
([20ed606](https://github.com/carlok/diaz-modulus-lean/commit/20ed606)) — and their
headers had kept claiming that only imports, namespaces and theorem names were
rewritten, which stopped being true with the bump. They now carry a sentence saying so
([7633db9](https://github.com/carlok/diaz-modulus-lean/commit/7633db9)). `scripts/Audit.lean`
also checks the axioms of the two interpolation obstructions now, alongside the headline
results, and the landrun wrapper accepts the delimiter the newer Comparator passes to it
([a97286b](https://github.com/carlok/diaz-modulus-lean/commit/a97286b)).
