---
title: "LeanFrontier: documentation proposals from anyone, a merge queue, and the launcher A/B suspended"
date: 2026-09-24
tags: [lean4, project, github]
---

The receiver's own day in [LeanFrontier](https://carlok.github.io/LeanFrontier/) was
governance rather than mathematics. A pull request whose every changed path is a Markdown
file under `docs/` is now a **documentation proposal**
([#291](https://github.com/carlok/LeanFrontier/pull/291)): no claim, no Lean, no build, and
the three stages that build or run candidate code are gated off, so a prose change costs one
short job instead of a Docker build and a Mathlib fetch — decided from the changed paths and
never from the branch name, with `docs/catalogue/` and `docs/website/` excluded because one
is generated from the corpus and the other publishes under the project's name. The friction
it removes was real and twice theirs:
[#290](https://github.com/carlok/LeanFrontier/pull/290) carries a contributor's rewritten
`docs/CONTRIBUTION-DIRECTIONS.md` with their authorship after the OWNER gate had refused it,
leaving six open directions and marking the ones that have landed.

[#300](https://github.com/carlok/LeanFrontier/pull/300) moves the merge sequencing out of a
local scratchpad and into the repository: a `workflow_dispatch` queue that waits for the
generators' own pull requests, updates each branch from `compare/...behind_by` rather than
`mergeStateStatus`, merges only what GitHub already reports `CLEAN`, stops on a genuine check
failure, and never overrides — which is the manual work that took 4 to 11 minutes per
submission and sequenced nineteen of them by hand on 22 September.
[#302](https://github.com/carlok/LeanFrontier/pull/302) writes down the threat model that
makes this defensible: what the receiver guarantees, six failure modes found in practice with
the fix for each, the trust boundaries, and — stated plainly — what remains unguarded, prose
and maintenance pull requests among them.

The experiment changed too. The pre-registered launcher A/B is
[suspended](https://github.com/carlok/LeanFrontier/pull/280): 3 of its 36 arm-tagged
submissions ever arrived, all of them on 20 August, none in the 34 days since the loop client
that assigned arms stopped running, so comparing A=2 against B=1 inside a corpus that is 95%
untagged would be arithmetic rather than evidence. The arms, metric and power table stay in
place so the test can be revived with a new dated section, and what replaces it is an
observational accumulation series over the whole corpus — edges, modules, edges per module,
connected share, in-degree and depth — with its three limits stated before the data was read,
including the one that dates the add-only rule: from 22 September every accepted extension
must add an import edge, which is convenient for the metric and therefore discounted rather
than celebrated. [The generator](https://github.com/carlok/LeanFrontier/pull/301) followed
the same day.
