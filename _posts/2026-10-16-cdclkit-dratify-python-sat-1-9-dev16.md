---
title: "cdclkit and dratify: python-sat 1.9.dev16 fixes the truncated CaDiCaL proofs"
date: 2026-10-16
tags: [tool, security]
---

The upstream bug that `dratify`'s `fflush` workaround existed for is fixed: `python-sat` 1.9.dev16 resolves [pysathq/pysat#233](https://github.com/pysathq/pysat/issues/233), the truncated CaDiCaL proof files that made most of PySAT's refutations fail to verify until the writer was flushed. Re-measured on the same 50 `uuf100` instances, 50 of 50 now verify on all four CaDiCaL versions with no flush at all, against 4–8 of 50 on 1.9.dev15; the workaround stays, marked as needed only for older versions, and the changelog catches up ([af19023](https://github.com/carlok/dratify/commit/af19023)). [cdclkit](https://github.com/carlok/cdclkit)'s roadmap records the confirmation, which closes the item the same chase had opened there ([5a8fe71](https://github.com/carlok/cdclkit/commit/5a8fe71)).
