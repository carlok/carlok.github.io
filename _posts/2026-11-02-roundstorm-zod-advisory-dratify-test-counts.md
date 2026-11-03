---
title: "roundstorm takes zod 4.6.7 for an advisory; dratify's README catches up with its test suite"
date: 2026-11-02
tags: [security, tool]
---

[roundstorm](https://github.com/carlok/roundstorm) moved its transitive `zod` to 4.6.7 for GHSA-mrhx-c7xc-m3w5, a lockfile-only change — `package-lock.json`, three lines added and eighteen removed, refresh of the optional `libc` metadata included ([f23e9bb](https://github.com/carlok/roundstorm/commit/f23e9bb)).

[dratify](https://github.com/carlok/dratify)'s README had been quoting the suite as it stood before the last two rounds of tests: it now says 172 tests rather than 163, and 145 in the dependency-free job rather than 113, against the same 90% statement coverage with an enforced floor of 80%, 25 tests needing a native checker and two needing `python-sat` ([2cc1976](https://github.com/carlok/dratify/commit/2cc1976), [#13](https://github.com/carlok/dratify/pull/13)).
