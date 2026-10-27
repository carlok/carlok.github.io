---
title: "forgepulse: two certificate-trust advisories closed, and the two that cannot be"
date: 2026-10-26
tags: [rust, security]
---

[forgepulse](https://github.com/carlok/forgepulse) took the transitive TLS bump for RUSTSEC-2026-0381 and RUSTSEC-2026-0382: `webpki-roots` 1.0.9 → 1.0.11 and `rustls-webpki` 0.103.15 → 0.103.16, lockfile only, no manifest change ([#6](https://github.com/carlok/forgepulse/pull/6), [2782e74](https://github.com/carlok/forgepulse/commit/2782e74)). `cargo audit` goes from three vulnerabilities to one — RUSTSEC-2023-0071 in `rsa`, which has no upstream fix — plus a tokio unsoundness warning, RUSTSEC-2026-0386, that waits on a patched release; the workspace's 54 tests pass either side of the bump.

The frontend followed the same day: `vitest` and `@vitest/coverage-v8` 4.1.11 → 4.1.12 for GHSA-xp26-3454-mjgp — a Windows backslash traversal that gets past `@vitest/mocker`'s redirect allow-list — and `vite` 6.4.3 → 6.4.5 so that `pnpm audit` comes back clean ([#5](https://github.com/carlok/forgepulse/pull/5), [ddd1dcf](https://github.com/carlok/forgepulse/commit/ddd1dcf)), with coverage unchanged at 98.66% statements.
