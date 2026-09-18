---
title: "unused-assumptions: the patches are not a set, and one written off was still true"
date: 2026-09-06
tags: [lean4, math, research]
---

Building a branch from all 36 weakenings in
[unused-assumptions](https://github.com/carlok/unused-assumptions)
[applied only 28](https://github.com/carlok/unused-assumptions/commit/caac8f4), and the
eight that did not apply are not all failures: two patches for `Indicator.lean` and three
for `Untop0.lean` rewrite the same variable line in different directions — one weakening
the algebraic class, another the order — so they are alternatives rather than additions,
and applied in sequence the first moves the context and the rest silently do not apply.
`patches/README.md` now says so, with the further caveat that a file carrying two
weakenings at once is a combination nothing here has compiled, since
`REPORT-master.json` is per-patch and not per-combination, and three tests hold the line:
alternatives must be documented wherever a pair rewrites one line, every patch touches
exactly one file, and every changed line is a variable line.

Another patch had been
[written off as superseded and still holds](https://github.com/carlok/unused-assumptions/commit/5f0366b):
`Topology/EMetricSpace/Pi.lean` was dropped from the master re-check because #42688
refactored the file and the patch text stopped applying, but against the refactored file
both binders can be replaced by `[EDist a]` and the file rebuilds at `633b366493` —
caught by Snir Broshi reading the demonstration branch and confirmed here by recompiling.
`ENGINEERING.md` now records what the durability run got wrong: it asked
`git apply --check` and let "does not apply" stand for "no longer holds", a substitution
every other stage of the project refuses because only the compiler decides. The
[note's counts follow](https://github.com/carlok/unused-assumptions/commit/c1c029a):
the paragraph that pooled them now separates the 34 findings that survive at `633b366493`
from the 33 patches that do, and names who caught the misfiled one — a reader of the
published branch finding what the pipeline had written off being, as the note puts it,
the strongest argument in the section for publishing the branch at all.

Two results in that note were measured by the companion project, and the citation now
[carries its URL](https://github.com/carlok/unused-assumptions/commit/1ab1638) — the
bibliography entry, the `data/root-invariance.jsonl` row and the `ENGINEERING.md` entry
that credits it for finding the open-directive defect all point at
[unstated-conclusions](https://github.com/carlok/unstated-conclusions), which at the time
of writing did not resolve yet: the reference went in before the DOI froze the PDF,
because adding a citation target afterwards means a new version rather than an edit.
