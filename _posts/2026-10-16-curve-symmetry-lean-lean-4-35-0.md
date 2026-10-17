---
title: "curve-symmetry-lean moves to Lean 4.35.0, and six statements need new parentheses"
date: 2026-10-16
tags: [lean4, math]
---

[curve-symmetry-lean](https://github.com/carlok/curve-symmetry-lean) moved to Lean 4.35.0 and Mathlib `v4.35.0`, 651 Mathlib commits past the `5ed2965` of v4.34.0, and the move is more than two lock files: five modules changed, one for the `SetLike.exists_of_lt` deprecation now spelled `IsConcreteLE.exists_of_lt`, and six statements across `PlaceUniformizers` and `InfinityDifferentials` where a singleton `{f a (b)}` written across lines began to parse as the start of a set-builder and needed to be written `{(f a (b))}` — a change of spelling that elaborates to the same statement ([a2c13b7](https://github.com/carlok/curve-symmetry-lean/commit/a2c13b7)). No declaration was added, removed or renamed, the audit stays at 2,058, and none of the 30 modules shared with the public [sharp-symmetry-bounds-lean](https://github.com/carlok/sharp-symmetry-bounds-lean) repository changed. `verification/lean-v4.35.md` records the move, the Prove2Me copy stays on Lean v4.33.1 with its mission record untouched, and a follow-up commit records the passing CI runs ([18d3984](https://github.com/carlok/curve-symmetry-lean/commit/18d3984)).
