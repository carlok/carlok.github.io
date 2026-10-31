---
title: "contributed to The Alien Space of Science and joserfc: where the idea went, and a one-second JWT bug"
date: 2026-10-30
tags: [contribution, security]
---

Two things went upstream from [alien-hunt](/blog/2026/10/30/alien-hunt-public/). On [alejandrohdez00/alien-space-of-science](https://github.com/alejandrohdez00/alien-space-of-science) — the paper and code the sampler is adapted from — [issue #2](https://github.com/alejandrohdez00/alien-space-of-science/issues/2) says where the idea was taken: what replaces the paper's trained coherence and availability models, the two results that survived a reproducer, and the two that did not. It asks for nothing.

On [authlib/joserfc](https://github.com/authlib/joserfc), [pull #109](https://github.com/authlib/joserfc/pull/109) turns `<` into `<=` in `JWTClaimsRegistry.validate_exp`. RFC 7519 §4.1.4 defines `exp` as the time "on or after which the JWT MUST NOT be accepted", but the check raised only when `exp < now - leeway`, so a token was still accepted during the second in which `exp == now`, and for a leeway window one second longer than the caller asked for. `nbf` and `iat` already follow the RFC; the new test checks both edges with and without a leeway, fails on `main` and passes with the fix, and the 297-test suite, `ruff check`, `ruff format --check` and `mypy` are clean. The effect is at most one extra second of validity, so it went in as a plain pull request rather than through the Security tab.
