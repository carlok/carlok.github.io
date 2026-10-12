---
title: "diaz-modulus-lean: every involution of the u-line, and a conjugation-stable space with no progression"
date: 2026-10-12
tags: [math, lean4]
---

Two research sprints landed in
[diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean), each
formalised the same day it was answered and each published as a companion-note
version. R9 extends the two-pole family to every Möbius involution of the
u-line: for `u ∉ Q̄` and the orbit pencil `q₁, q₂` of an involution, the space
`H₀ + Σᵢ Q̄ q₁(u)ⁱq₂(u)³⁻ⁱ/(u l₁(u) l₂(u))` carries a 2×3 configuration — the
progression with ratio `q₁(u)/q₂(u)` — and contains none of `u²`, `u⁻²` or
`1/(u − b)`, so no four-dimensional space of Theorem B inside it carries one.
It is Theorem 5.9 of
[note v1.23](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.23),
four nodes and 393 results
([8336e66](https://github.com/carlok/diaz-modulus-lean/commit/8336e66)).

R11 answers the question R9 left open, and the answer is yes: there is a
five-dimensional space above `H₀` that is stable under complex conjugation, that
carries a configuration Theorem B's four-dimensional spaces cannot see, and that
contains no progression at all. The real pencil spaces — the span of `1, u, ū, f`
and `f/(s + λu)`, with `s² = uū` real and `|λ| = 1` — are exactly the
conjugation-equivariant degree-one spaces, and at `λ = 1`, `f = u²/s² + s²/u²`
the member is invisible and its polar divisor has degree 5, so the R5 conjecture
fails even for conjugation-stable spaces; the converse in Proposition 5.11 is
one conjugation applied twice. Index one of the earlier case turns out to be
visible, and Kirby's weak Schanuel conjecture at `n = 2` together with Schanuel
over the kernel `2πiQ` at `n = 1` implies Diaz's conjecture — the second
hypothesis contains the algebraic independence of `e` and π, which is open
([note v1.24](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.24),
seven nodes and the full 400 results,
[d5d87c3](https://github.com/carlok/diaz-modulus-lean/commit/d5d87c3)). The
blueprint gained the chapters, 176 to 183 nodes, and both missions are logged on
the [prove2me-logs](https://github.com/carlok/prove2me-logs) board
([862ada6](https://github.com/carlok/prove2me-logs/commit/862ada6),
[24dafea](https://github.com/carlok/prove2me-logs/commit/24dafea)).
