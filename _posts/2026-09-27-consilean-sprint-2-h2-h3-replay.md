---
title: "consilean: the second H2 ranking, a read-only H3 replay, and why the frozen deprecations cannot be H3 links"
date: 2026-09-27
tags: [lean4, math, tool]
---

Sprint 2 of [consilean](https://github.com/carlok/consilean) — the scorer of Lean
statement pairs by similarity and dependency-graph distance, with the kernel left
as the authority on whether a candidate connection holds — recorded a second H2
ranking and a read-only replay of the H3 axis against Mathlib v4.28.0, with the
run reports generated into `docs/`
([1592971](https://github.com/carlok/consilean/commit/1592971)). One negative
result is recorded rather than buried: the frozen Mathlib deprecation pairs cannot
serve as later H3 links, because every `since` date is already earlier than the
Mathlib revision that was scored
([39a5a75](https://github.com/carlok/consilean/commit/39a5a75)). The wider
statement reader therefore stays on the frozen deprecation set, and the duplicate
list stays empty — none of the recovered pairs closed on the later revision.
