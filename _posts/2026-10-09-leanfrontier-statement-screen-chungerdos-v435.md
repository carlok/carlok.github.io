---
title: "LeanFrontier: a weekly screen that every accepted statement can be stated as written"
date: 2026-10-09
tags: [lean4, math, project]
---

Four silent bugs in how [LeanFrontier](https://carlok.github.io/LeanFrontier/)'s
receiver reads a theorem out of its source were found in one week — two of them
by accident, while writing field notes — so the one-off corpus screen is now a
guard: `tools/screen_statements.py` states every accepted entrypoint with
`sorry` in exactly the probe's context and classifies each result as `stated`,
`own definition` (the statement mentions a name its own module defines, which
the probe deliberately cannot see) or `other`, and any `other` fails the job.
`.github/workflows/screen-statements.yml` builds the corpus in the validator
image, screens it offline with `--network none --read-only --cap-drop ALL`, and
runs weekly as well as on the relevant pull requests
([#498](https://github.com/carlok/LeanFrontier/pull/498)).

The ChungErdos module was the only break in a dry-run audit against Mathlib
v4.35.0-rc4: v4.35 changed `MemLp.indicator` to take a `NullMeasurableSet`, so
the proof now tries both forms and a comment says to keep only the new one once
v4.34 is gone. A maintenance PR does not go through the receiver, so the change
came with the evidence that only a proof moved — the same 1184 declarations
before and after, identical canonical types, kinds and axioms
([#500](https://github.com/carlok/LeanFrontier/pull/500)). The contribution
directions were refreshed for a corpus that has taken 22 submissions since the
27 September roadmap, removing the five directions that have landed
([#496](https://github.com/carlok/LeanFrontier/pull/496)), and
`docs/dataset.md` now explains what the probe outcomes mean before and after the
7 October reading fix, for anyone using `corpus-v1`
([#497](https://github.com/carlok/LeanFrontier/pull/497)).
