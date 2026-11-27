---
title: "dratify: the native suite now runs in CI, the release workflow tests before it publishes, and v0.1.11 has a release page"
date: 2026-11-26
tags: [rust, tool]
---

[dratify](https://github.com/carlok/dratify)'s native side was being tested less than it looked. `make test-native` asserted `native_available()`, which is False until a checker is registered, so it failed even with the Rust accelerator installed, and CI's differential job ran two modules, so the native twins of the 0.1.11 fix tests — deleted reasons, the direct checker, the literal bound, proof stream, refutation is final, repeated literals — skipped on every run. `tests/run_native_suite.sh` now runs the whole suite against the Rust checker and fails only if a test that needs it skipped, CI calls that script, and a new job checks the declared `rust-version` ([e88674e](https://github.com/carlok/dratify/commit/e88674e), [33e5709](https://github.com/carlok/dratify/commit/33e5709)).

The release path got the same treatment: `rust-test` now gates both publish jobs, so a crate that fails cannot follow a PyPI upload of the same version, and a single job with write access creates the GitHub Release from the version's CHANGELOG section, a no-op on a re-run ([bbcf246](https://github.com/carlok/dratify/commit/bbcf246)). [v0.1.11](https://github.com/carlok/dratify/releases/tag/v0.1.11) now has that entry, published on 26 November with its three advisories linked and its changelog beside them — the fixes themselves were [described on 9 November](/blog/2026/11/09/dratify-0-1-11-deletion-of-a-reason-clause/) and what was missing was the release page.

A regression test for `d 0` being ignored and the next line read, on both engines, came with them, along with documentation that says where the soundness campaign's commits now live and when a deletion is ignored on the Rust side ([061d783](https://github.com/carlok/dratify/commit/061d783), [bb0bd09](https://github.com/carlok/dratify/commit/bb0bd09)).
