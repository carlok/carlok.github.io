---
title: "diaz-modulus-lean: the companion note reaches 1.0, where the case analysis ends"
date: 2026-09-21
tags: [lean4, math, research]
---

The companion note to [diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean)
is now fixed at [stable version 1.0](https://github.com/carlok/diaz-modulus-lean/releases/tag/note-v1.0)
([f4cca8b](https://github.com/carlok/diaz-modulus-lean/commit/f4cca8b)) — the point
at which the formal case analysis stops rather than a point along it. Every branch
of Diaz's conjecture is either closed by a machine-checked proof or reduced, by a
machine-checked reduction, to one of three statements: that `e^{-iγ/π}` is
transcendental for real algebraic `γ ≠ 0`, that `e^{β/π}` is transcendental for
real algebraic `β ≠ 0`, and that `|u|` is transcendental for a generic conjugate
pair of logarithms, which is the conjecture itself. All three follow from the
strong four exponentials conjecture, and the note says so, with the section the
abstract had always promised and the body never contained; section 5 gains the two
interpolation obstructions proved on 19 September.

The release records its own checks: the 33 identifiers of Appendix A were verified
against the platform by script with zero mismatches, and 166 of 166 proved results
are mirrored, with `lake build Diaz` clean and only `propext`, `Classical.choice`
and `Quot.sound` behind them. The axiom list is now checked by
[CI](https://github.com/carlok/diaz-modulus-lean/commit/b695a9c) instead of by hand,
and [prove2me-logs](https://github.com/carlok/prove2me-logs/commit/2fe5a0a) mirrors
the note at the same tag.
