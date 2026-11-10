---
title: "topshift-trend: under the new Python 3.13 builder the bot could not start at all, and the fault is a slot python-telegram-bot forgot to declare"
date: 2026-11-08
tags: [bot, podman]
---

Two days after [moving the image to a Python 3.13 builder](/blog/2026/11/06/topshift-trend-distroless-debian-13-python-313/), production never came up: every container start died the same way, over 164k restarts, in `Application.builder().build()` → `Updater.__init__` with `AttributeError: '_Updater__polling_cleanup_cb'`. The fault is [python-telegram-bot#4127](https://github.com/python-telegram-bot/python-telegram-bot/issues/4127) — `Updater` declares `__slots__` but assigns `__polling_cleanup_cb` without listing it, and below 3.13 the `AsyncContextManager` base still supplied a `__dict__` for the stray attribute; 3.13 does not, so construction fails before polling starts ([#13](https://github.com/carlok/topshift-trend/pull/13), [0563105](https://github.com/carlok/topshift-trend/commit/0563105)).

The constraint moves from `>=20.7,<21.0` to `>=21.11,<22.0` (resolving to 21.11.1), with no `Containerfile` change, since the rebuild installs from `pyproject.toml`. Reproducers on 3.13.18 pinned the boundary first — 20.8 fails, 21.7 and 21.11 pass — and `tests/test_ptb_startup.py` now keeps it: it constructs `Updater` directly, and on 3.13+ builds the real application, with no mocks and no network; the suite is 47 passed at 94.08% coverage on 3.13 and 46 passed with the 3.13-only test skipped on 3.12.
