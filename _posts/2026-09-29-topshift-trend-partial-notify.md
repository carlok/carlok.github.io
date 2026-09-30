---
title: "topshift-trend: a transient failure no longer wipes out what was already delivered"
date: 2026-09-29
tags: [telegram, bot, tool]
---

A scheduled notify pass in
[topshift-trend](https://github.com/carlok/topshift-trend) can now fail halfway
without repeating itself: per-chat deliveries are recorded as they succeed, so
the next run skips the links a chat already received and retries only the ones
that never went out, and the global cooldown baseline advances only after a
clean pass
([0ce1688](https://github.com/carlok/topshift-trend/commit/0ce1688),
[PR #9](https://github.com/carlok/topshift-trend/pull/9)). Before this, one
transient Telegram error in the middle of a batch could resend everything that
had already arrived. A ruff `UP035` fix — `Mapping` imported from
`collections.abc` — rode along.
