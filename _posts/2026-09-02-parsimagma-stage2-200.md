---
title: "parsimagma v1.0-stage2: 200/200 on the Stage 2 sample set"
date: 2026-09-02
tags: [math, tool, research]
---

[parsimagma](https://github.com/carlok/parsimagma) is tagged
[v1.0-stage2](https://github.com/carlok/parsimagma/releases/tag/v1.0-stage2):
one standard-library-only Python file — no database, no lookup table, no LLM
call — reaches 200/200 on the organizer's 200-problem sample set, confirmed by
two independent runs agreeing problem for problem and explicitly not the
private graded set. Three search mechanisms split the work: finite model search
refutes false implications cell by cell, critical-pair completion proves most
of the true ones, and ordered superposition under a Knuth–Bendix ordering takes
the rest. Every derived equation carries its replayable derivation, paths are
double-checked before any Lean is written, and certificates are emitted from
the inference DAG rather than flattened — 13,728 bytes against 3,634,949 on the
hardest problem.
