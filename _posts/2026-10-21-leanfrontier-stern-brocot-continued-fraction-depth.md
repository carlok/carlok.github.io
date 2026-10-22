---
title: "LeanFrontier: Stern–Brocot depth is the sum of the continued-fraction coefficients"
date: 2026-10-21
tags: [lean4, math]
---

[#542](https://github.com/carlok/LeanFrontier/pull/542) proves that for every Boolean path into the Stern–Brocot tree, the sum of the regular continued-fraction coefficients of the rational the path represents is the number of path edges plus one — `(regularCoefficients path).sum = path.length + 1` — quantifying the classical correspondence between a rational's depth in the tree and the total size of the quotients in its Euclidean expansion, with the empty-root convention and the leading zero for fractions below one handled uniformly ([1e72baf](https://github.com/carlok/LeanFrontier/commit/1e72baf)).

The submission by [qazW12345](https://github.com/qazW12345) is a consumption piece rather than a fresh start: the proof runs through accepted corpus lemmas `pathQuotients_eq_runLengthEncode` (the terminal Euclidean quotient is the final maximal run length plus one), `expandRuns_runLengthEncode` (encoded runs expand to the original path) and `regularCoefficients_runs`, plus one local list-sum lemma for incrementing a last element. It adds exactly two files — `LeanFrontier/NumberTheory/SternBrocot/ContinuedFractionDepth.lean` and its submission record — with a single public theorem entrypoint, three private technical lemmas, no alternative path encoding and no modification to any accepted file.

Machine-authored by GPT-6 on Mathlib `v4.35.0`, the source passed the fork's full receiver with `accepted: true`, empty diagnostics, kernel replay and no disallowed axioms, and merged on 2026-10-21 ([a8ba582](https://github.com/carlok/LeanFrontier/commit/a8ba582)); the day's other upstream movement was an umbrella sync and a receiver observation record. Field notes are at [carlok.github.io/LeanFrontier/notes](https://carlok.github.io/LeanFrontier/notes/).
