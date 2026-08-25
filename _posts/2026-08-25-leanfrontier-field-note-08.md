---
title: "LeanFrontier: nobody chose the version (Field Note 08)"
date: 2026-08-25
tags: [lean4, math, project]
---

[LeanFrontier](https://github.com/carlok/LeanFrontier)'s
[Field Note 08](https://carlok.github.io/LeanFrontier/notes/) records the corpus
moving to Mathlib v4.33.1 on schedule, with the version chosen by nobody: the
upgrade pipeline rebuilt the fingerprint index, re-audited all 114 entrypoints,
replayed the kernel, and opened the pull request itself — a person only merged
it. Getting there took three stacked defects, each invisible until the one
before it was fixed, the best being a validator that refused the upgrade over
bytecode it had compiled into its own working tree while running. A fourth
outside contributor also sent in a submission, still open pending a rebase onto
the new toolchain, and no acceptance was weakened by the upgrade.
