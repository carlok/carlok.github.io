---
title: "dratify: parse_dimacs gives a body literal the header's bound, and counts the tautologies CNF.add drops"
date: 2026-10-25
tags: [tool]
---

Two holes in [`parse_dimacs`](https://github.com/carlok/dratify) closed on 25 October. The header guard refused `p cnf 3000000 0`, but the body form `1 3000000 0` — twelve characters — set `CNF.nvars` to 3,000,000, which is what sizes the checker's arrays; a literal is now bounded like the header, by `max(len(text), HEADER_VARS_FLOOR)`, checked before it is stored, with the `ValueError` naming the line and the literal (CWE-789, [#5](https://github.com/carlok/dratify/pull/5), [7bf8057](https://github.com/carlok/dratify/commit/7bf8057)).

The second is a counting bug in the other direction: `CNF.add` drops a tautological clause, so `p cnf 2 2` with `1 -1 0` and `1 2 0` matched two declared clauses against the one kept, `strict=True` raised and `header_mismatch` was `(2, 1)`; the dropped tautologies are now added back before the comparison (CWE-697, [#6](https://github.com/carlok/dratify/pull/6), [d17d351](https://github.com/carlok/dratify/commit/d17d351)). Both changes were written by a model and judged by the Provex App in run `hz-dratify-1`, each with a test that fails before and passes after — 141 and 140 passing against 136 on 0.1.10, which remains the newest tag.
