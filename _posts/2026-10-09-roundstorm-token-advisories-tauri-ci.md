---
title: "roundstorm: a per-launch token, four cleared advisories, and a Tauri shell that compiles in CI"
date: 2026-10-09
tags: [tool, security]
---

[roundstorm](https://github.com/carlok/roundstorm)'s desktop app now generates
32 random bytes on every launch, hands them to the daemon as `ROUNDSTORM_TOKEN`
and injects them into its own page, and the daemon refuses `/api` and `/ws`
without it — unset, the headless CLI and every script behave exactly as before.
It is narrower than "auth", and `SECURITY.md` now says so: it stops another
process on the loopback socket and another user on a shared machine, and makes
`ROUNDSTORM_HOST=0.0.0.0` defensible, but not malware running as the user
([17618e7](https://github.com/carlok/roundstorm/commit/17618e7)).

GitHub's alerts reported four advisories — two critical — within minutes of a
push, none of which an `npm audit` an hour earlier knew about: `proxy-addr` and
`shell-quote` (critical) and `source-map-js` (high), all lockfile-only, plus
three copies of `katex` collapsed onto the top-level 0.19.0 with an `overrides`
entry after comparing the renderer rather than assuming it
([8d82e2f](https://github.com/carlok/roundstorm/commit/8d82e2f)). Nothing in CI
compiled Rust, so a shell dependency bump showed green while proving nothing —
`cargo check --locked` now runs (macOS only, since the project ships no Linux
target) ([c7a1040](https://github.com/carlok/roundstorm/commit/c7a1040)), and the
headless path stopped giving plausible wrong answers: unknown config keys are
refused with a did-you-mean, a mistyped brain or persona is rejected, and the
CLI no longer prints the previous run's conclusion when synthesis returns
nothing ([dc0039b](https://github.com/carlok/roundstorm/commit/dc0039b)).
