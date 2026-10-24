---
title: "cdclkit: the scaling test steps 16x so a linear engine still fails it; dratify 0.1.8 is a documentation release"
date: 2026-10-23
tags: [tool]
---

The scaling test in [cdclkit](https://github.com/carlok/cdclkit) watched for a regression by quadrupling the variables and expecting more than linear time, and a macOS runner duly reported 8.3x for 4x the variables on native runs of 4 and 32 ms — cache growth and timer noise, with a linear engine already sitting at 4.5x. Rather than tighten a threshold against noise, the test now steps by 16x with a limit of 64, where linear is about 20x and quadratic about 256x ([b59350d](https://github.com/carlok/cdclkit/commit/b59350d)). It was checked against the engine before the fix: cdclkit 0.1.4 measures 252x on native runs and 218x in Python at the new step, so the test still catches what it exists to catch.

[dratify](https://github.com/carlok/dratify) is tagged [v0.1.8](https://github.com/carlok/dratify/tree/v0.1.8) as a documentation release, and nothing else: PyPI and docs.rs were still serving 0.1.7's text, where the README warned PySAT users that their CaDiCaL proofs arrive truncated — true before `python-sat` 1.9.dev16, which [fixed it](/blog/2026/10/16/cdclkit-dratify-python-sat-1-9-dev16/) — and the note on `Checker` memory growing with the largest literal had never been published at all ([ed00215](https://github.com/carlok/dratify/commit/ed00215)). Parsing and checking are untouched. Both repositories also let their CI be re-run by hand, written the day `ubuntu-latest` started moving to Ubuntu 26, so a workflow can be retried against a runner image that changed under a green build ([cdclkit](https://github.com/carlok/cdclkit/commit/34fdb14), [dratify](https://github.com/carlok/dratify/commit/2de7704)).
