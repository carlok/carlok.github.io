---
title: "slop-audit: a local harness for AI-slop signals and formulaic prose"
date: 2026-09-13
tags: [tool, project]
---

[slop-audit](https://github.com/carlok/slop-audit) is now public: a Python
harness that scores a piece of prose for AI-slop and formulaic style, general
writing issues and descriptive stats, and — kept strictly separate from all of
it — local AI-authorship detector signals. Nothing leaves the machine: there
are no hosted detector APIs and no remote LLM touching the target text, with
the network used only for installs and optional model-weight downloads. A run
produces a **Slop Index** (0–100 plus band) from the slop tools and linters
([05e1527](https://github.com/carlok/slop-audit/commit/05e1527)), deterministic
edit suggestions quoted from the tools that would lower it — no LLM rewrite of
the prose ([7bcdcc3](https://github.com/carlok/slop-audit/commit/7bcdcc3)) —
and a per-tool matrix reporting `OK` / `NOT_RUN` / `ERROR` with the exact
reason, so a tool that failed never invents a score.

The first day's work built the machinery underneath: adapter subprocess
helpers and a registry ([dde644f](https://github.com/carlok/slop-audit/commit/dde644f)),
the five slop tool adapters with Vale and custom Slop styles
([8858c94](https://github.com/carlok/slop-audit/commit/8858c94),
[ba9a9d7](https://github.com/carlok/slop-audit/commit/ba9a9d7)), a restartable
audit runner with a tool cache and best-effort installation for the whole
toolchain ([ced3f8d](https://github.com/carlok/slop-audit/commit/ced3f8d),
[affbec6](https://github.com/carlok/slop-audit/commit/affbec6)), and a
family-aware **AI-Likeness Ensemble** with independent agreement helpers that
is never merged into the Slop Index
([ce2bbab](https://github.com/carlok/slop-audit/commit/ce2bbab)). Vendored
copies of Vale, Harper and write-good were dropped the same day in favour of
syncing on install ([5ce0611](https://github.com/carlok/slop-audit/commit/5ce0611)),
and the reporting language stays concentration-language throughout: N of M
local detectors classifying AI-like, never a claim that the text was written by
AI.
