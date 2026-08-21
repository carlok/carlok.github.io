---
title: "lean-corpus-density: does machine mathematics accumulate?"
date: 2026-08-21
tags: [lean4, research, project]
---

[lean-corpus-density](https://github.com/carlok/lean-corpus-density) is a new,
reproducible measurement of dependency density in Lean 4 corpora, human and
machine-generated. Replaying Tau Ceti's commit history shows its internal
import density rising monotonically as it grew — 0.40 edges per module at ten
modules up to 1.55 at 2,314 — evidence that machine-generated mathematics
builds on itself rather than merely piling up. The whole analysis is
reproducible from file headers; no build is required.
