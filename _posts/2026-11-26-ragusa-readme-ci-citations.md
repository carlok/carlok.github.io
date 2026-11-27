---
title: "ragusa: a README that says what to type, CI that runs it, and citations checked against the sources"
date: 2026-11-26
tags: [math, rust]
---

[ragusa](https://github.com/carlok/ragusa) spent 26 November on what a launch post leaves implicit. The README now lists the requirements, every `make` target, the external inputs each project needs and where the results are written, with a `CITATION.cff` beside it; `PROMPT.md` is marked as the original brief and lost its machine-specific appendix; stale status lines, licence leftovers and other small inaccuracies were fixed ([7cd51d0](https://github.com/carlok/ragusa/commit/7cd51d0), [427a7d2](https://github.com/carlok/ragusa/commit/427a7d2), [6349161](https://github.com/carlok/ragusa/commit/6349161)).

CI now does what the README tells you to: `make test` on ubuntu plus rustfmt, clippy and a check that the rendered report is not stale, with the workflow actions moved to checkout v7 and setup-uv v10.3.3 because the old ones targeted the deprecated Node 20 ([fa27d98](https://github.com/carlok/ragusa/commit/fa27d98), [bdda164](https://github.com/carlok/ragusa/commit/bdda164)). All of it was exercised by building and testing on a fresh machine rather than the one it was written on ([688b9c3](https://github.com/carlok/ragusa/commit/688b9c3)).

The prose got the same audit. Statements about what TxGraffiti's and AutoGraphForge's filters do now read as the project's reading of their code rather than as fact, and the citations were checked against the primary sources, with credit added for Jablonowski, Kasprzyk and parsimagma ([01b17a8](https://github.com/carlok/ragusa/commit/01b17a8), [4f76349](https://github.com/carlok/ragusa/commit/4f76349)).
