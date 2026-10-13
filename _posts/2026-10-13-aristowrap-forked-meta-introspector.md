---
title: "aristowrap was forked by meta-introspector"
date: 2026-10-13
tags: [lean4, project]
---

[carlok/aristowrap](https://github.com/carlok/aristowrap) — the Docker-first
wrapper that submits a Lean 4 project to Harmonic's Aristotle and typechecks the
returned archive, so no elan, Lake or Python is needed on the host — was forked
by [meta-introspector](https://github.com/meta-introspector), whose fork is
[here](https://github.com/meta-introspector/aristowrap). meta-introspector builds
its own Aristotle and Lean tooling around the same problem — an
[Aristotle CLI in Rust](https://github.com/meta-introspector/aristotle-cli-rs),
[lean-worker](https://github.com/meta-introspector/lean-worker) and a registry
for Lean workers — so the fork arrives from someone already working in the
space. No changes have come back from it.
