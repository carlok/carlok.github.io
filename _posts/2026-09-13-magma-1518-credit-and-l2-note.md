---
title: "magma-1518-obstruction-lean: the November 2024 thread gets the credit, and the l2_note catches up with its theorems"
date: 2026-09-13
tags: [lean4, math, research]
---

The [credit corrections](/blog/2026/09/10/magma-1518-palomar-attribution/) in
[magma-1518-obstruction-lean](https://github.com/carlok/magma-1518-obstruction-lean)
went a step further: every equivalence among the four 1518 targets was posted on the
Lean Zulip in November 2024 — Tao relating 47 and 614 through law 359, Tencer tying 817
to `S³x = x`, Bolan noting with Prover9 that 3862 implies the other three, and Nielsen
verifying with Vampire that all four agree under left cancellation — so
[3862 is no longer presented as an improvement over Tao's conjecture](https://github.com/carlok/magma-1518-obstruction-lean/commit/1ab7547),
which the earlier correction still called one, and what the repository adds is now
stated as the proof rather than the reduction.

The same pass brought the write-up in line with what it proves
([ea162fd](https://github.com/carlok/magma-1518-obstruction-lean/commit/ea162fd)): the
Questions section no longer asks what Theorem `thm:closure` and Theorem `thm:full`
already settle, the scope paragraph limits the gap to infinite bases instead of bases
carrying a one-generated submagma of nine or more elements, and the family section stops
calling the 15-element models generic when only two of the six are members. The six
models are numbered as members of Brox's enumeration, the description of their squaring
maps is credited to Le Floch who posted it, a stale Lean path in `prerequisites.tex` is
corrected, and the PDFs are rebuilt.
