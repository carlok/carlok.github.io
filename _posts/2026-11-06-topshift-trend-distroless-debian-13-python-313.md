---
title: "topshift-trend: the Distroless runtime moves up to Debian 13 and a Python 3.13 builder"
date: 2026-11-06
tags: [bot, podman]
---

Four days after [moving production to Distroless Python](/blog/2026/11/02/topshift-trend-distroless-runtime/), the [topshift-trend](https://github.com/carlok/topshift-trend) image is on the next base: a Python 3.13 builder stage, Distroless Debian 13 for the runtime, and pip 26.2.2 in the build ([60668b0](https://github.com/carlok/topshift-trend/commit/60668b0), [#12](https://github.com/carlok/topshift-trend/pull/12)). The point of the earlier change holds — no shell and no package manager in the shipped layer — and the interpreter in the venv still has to match the one that built it, which is what the pinned builder stage is for.
