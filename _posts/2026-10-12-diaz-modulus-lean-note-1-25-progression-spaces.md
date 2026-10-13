---
title: "diaz-modulus-lean: note v1.25 classifies the progression spaces, and the library reaches 403"
date: 2026-10-12
tags: [lean4, math, research]
---

The Diaz companion note is at
[v1.25](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.25),
which makes the classification of Remark 5.10 formal for a ratio rational in
`u`: a five-dimensional space spanned by `1, u, u⁻¹` and the four powers
`c·hᵏ` of a progression ratio `h = p(u)/q(u)` either contains `u²`, contains
`u⁻²`, contains some `(u − b)⁻¹` with `b` algebraic and non-zero, or is an
involution-pencil space
([8341107](https://github.com/carlok/diaz-modulus-lean/commit/8341107)). Two
steps carry it. The ratio's polynomials have degree at most two — an
embedding `Q̄(X) → ℂ` at `X ↦ u`, coprimality forcing `p ∣ num f` and
`q ∣ den f`, and Mathlib's Lüroth degree formula `[K(X) : K(f)] = max(deg num f,
deg den f)` — and a degree of exactly two makes the space an involution-pencil
space, `c hᵏ = κ pᵏ q³⁻ᵏ / (u l₁ l₂)` for two pencil members
`lᵢ = aᵢp + bᵢq`. Three new formal results, milestone 126, and the mirrored
project now holds all 403 proved results on Lean's three standard axioms; the
progression step (Bachoc–Serra–Zémor, Lemma 4) and the rationality of `h` stay
in the text rather than in Lean, and the classification was not found in the
sources read
([f8102b4](https://github.com/carlok/prove2me-logs/commit/f8102b4)).
