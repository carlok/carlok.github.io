---
title: "cdclkit: the trail copy stops going quadratic on decision-only searches"
date: 2026-10-09
tags: [security, tool]
---

[cdclkit](https://github.com/carlok/cdclkit)'s target-phase search copied the
whole trail into the target at every new deepest trail. The comment said
improvements become rare quickly, which is true once conflicts start and false
before: a search that makes many decisions without one improves on every
decision, so n decisions copied 1, 2, …, n entries — 65,536 declared variables
and one unit clause took 144 s in Python, 131,072 took 4.2 s natively, and each
4× in variables cost about 13–19×
([e43a4ac](https://github.com/carlok/cdclkit/commit/e43a4ac)). A counter now
records how much of the trail the target already holds, only the new suffix is
copied, and the target still ends up byte-for-byte what the full copy produced.

It had become a denial-of-service through a fix of the author's own: dratify
0.1.7 correctly accepts headers declaring up to 2²⁰ variables from a file of any
length, so a 22-byte file could cost cdclkit hours.
`tests/test_target_scaling.py` asserts that quadrupling the variables costs
closer to 4× than 16× on both engines — it measured 13.6× and 19.0× before the
fix; 65,536 variables now take 0.48 s, and 2²⁰ take 10 s in Python and 0.13 s
natively.
