---
title: "contributed to arminbiere/kissat: clause-section parse errors all point at line 1"
date: 2026-10-15
tags: [contribution, tool]
---

Opened [issue #83](https://github.com/arminbiere/kissat/issues/83) on [arminbiere/kissat](https://github.com/arminbiere/kissat), reporting that most parse errors in the clause section report line 1 whatever line they are actually on: an `x` on line 7 of a seven-line DIMACS file comes back as `kissat: error: x.cnf:1: parse error: expected digit or '-'`. The cause is in `parse_dimacs`, which counts lines in a local `lineno` and sets `*lineno_ptr = 1` once at the start, copying the local value back only in `NONL(...)` and on success — every other error path returns its message directly, so the caller prints the initial 1. The report proposes a sibling macro of `NONL` that assigns the counter before returning, notes that CaDiCaL 3.0.1 reports the right line on the same input, and records that it was reproduced by hand against kissat 4.0.4 and current master by an LLM-assisted analysis. It was found while testing a DIMACS parser against the SATLIB `uf*` files that end with `%`, which is also how [cdclkit closed the same roadmap item](/blog/2026/10/15/cdclkit-0-1-6-engine-selector/) without reporting the `%` upstream.
