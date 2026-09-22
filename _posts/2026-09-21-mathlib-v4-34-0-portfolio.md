---
title: "Seven Lean repositories move to Mathlib v4.34.0"
date: 2026-09-21
tags: [lean4, math]
---

The Lean toolchain and Mathlib moved to v4.34.0 across the portfolio in one pass.
[erdos-straus-offset-lean](https://github.com/carlok/erdos-straus-offset-lean/commit/aa79d27),
[magma-1518-obstruction-lean](https://github.com/carlok/magma-1518-obstruction-lean/commit/b77644e),
[moebius-transcendental-lean](https://github.com/carlok/moebius-transcendental-lean/commit/a356490) and
[sharp-symmetry-bounds-lean](https://github.com/carlok/sharp-symmetry-bounds-lean/commit/072599d)
took the bump together with a new CI job that audits the axioms their headline
theorems actually depend on, so a silently new dependency on `Classical.choice`
or worse would fail the build rather than sit in the proof term.
[inversive-geometry-lean](https://github.com/carlok/inversive-geometry-lean/commit/6585653)
took the same bump and its README's pinned version followed
([d512c1f](https://github.com/carlok/inversive-geometry-lean/commit/d512c1f)).

The two verifier repositories were rerun rather than merely bumped:
[unused-assumptions](https://github.com/carlok/unused-assumptions/commit/f2426b0)
re-verified its one-binder weakenings by compiling them at the new revision, and
[unstated-conclusions](https://github.com/carlok/unstated-conclusions/commit/ba71d0a)
reran Part 1. [LeanFrontier](https://carlok.github.io/LeanFrontier/notes/)'s own
weekly upgrade landed the same day, on the third attempt, and its field note
records what broke along the way: Mathlib's download cache was missing a compiled
module, and a re-audit job was running twice per head.
