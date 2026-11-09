---
title: "diaz-modulus-lean: a prior-art sweep of chapter 14's twenty entries, and the Li₂(1/2) line put right"
date: 2026-11-08
tags: [math, lean4, research]
---

[diaz-modulus-lean](https://github.com/carlok/diaz-modulus-lean) ran a desk search aimed at breaking each "not found" in chapter 14 of its blueprint, the list of results the library claims do not appear in the sources read. Of the twenty entries the sweep returns **5 `found`, 5 `found in part` and 10 `not found by this sweep`**, with none left as an unverified lead — and no statement was found printed as it stands anywhere, since every `found` is a printed theorem plus a derivation written by a verifier ([reports/prior-art-sweep-2026-11](https://github.com/carlok/diaz-modulus-lean/tree/master/reports/prior-art-sweep-2026-11), [#5](https://github.com/carlok/diaz-modulus-lean/pull/5)).

Theorem B leaves the not-routine list: its key step is in print under another name — Park in *Trans. AMS* 377, Park–Sim in *Math. Nachr.* 298, and Arbarello–Harris §2 — and the rest takes two lines by gcds, so entries 2, 3 and 4 move up to ranks 1–3. Entries 6, 9 and 14 settle as `found in part` on derivations from Bachoc–Serra–Zémor that the verifiers marked as not covered by the source alone, and entries 6, 8, 9, 14, 16, 17, 18 confirm "routine" each following quickly from a theorem already cited.

The correction that matters outside the table is entry 18: its source line said the irrationality of Li₂(1/2) is still open, and that "still open" is gone from the blueprint, the README and the note, replaced by the fact that two unrefereed 2026 preprints report it proved (Tan–Zhang, arXiv:2611.01066, Th. 1.3; Lai, arXiv:2610.06838). The Lean repositories those papers name were read but never built, and the sweep itself changed nothing — the edits applied are the author's ([08f4498](https://github.com/carlok/diaz-modulus-lean/commit/08f4498), [42235e8](https://github.com/carlok/diaz-modulus-lean/commit/42235e8)).
