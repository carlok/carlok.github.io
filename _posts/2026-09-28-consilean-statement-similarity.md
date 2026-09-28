---
title: "consilean is public: scoring Lean statements by similarity and dependency distance"
date: 2026-09-28
tags: [lean4, math, tool]
---

[consilean](https://github.com/carlok/consilean) is a new public Python
repository that scores pairs of formal statements in Lean corpora on two axes —
how similar they are, and how far apart they sit in the dependency graph.
Similar statements that sit near each other are duplicate candidates; similar
statements that sit far apart are candidate hidden connections, and Lean's
kernel stays the authority on whether a connection holds: a similarity score is
a pattern, not a claim.

The question comes from [@qazW12345](https://github.com/qazW12345), who
described the idea on [LeanFrontier pull request
340](https://github.com/carlok/LeanFrontier/pull/340) and set it aside over
token cost, expertise and licensing; the suggestion was to try it where a
checker can judge it, since the dependency graph is exact and no licensing
question exists. In its first day the repository
[bootstrapped the LeanFrontier pilot
baselines](https://github.com/carlok/consilean/commit/cf0cd98), ranked theorems
with a preregistered name-free Weisfeiler–Lehman score plus a normal form that
sends `IsSquare` in `ZMod` to an integer congruence
([acd5aac](https://github.com/carlok/consilean/commit/acd5aac)), froze Mathlib
deprecation pairs and measured the recall of the second axis
([663db61](https://github.com/carlok/consilean/commit/663db61)), and added a
Sprint 3 agent gate that runs without calling a model
([e8d916f](https://github.com/carlok/consilean/commit/e8d916f)).
