---
title: "portcullis: the remote script is read until EOF, so Phase 2's tail stops vanishing from the log"
date: 2026-10-24
tags: [security, tool]
---

[portcullis](https://github.com/carlok/portcullis) had a logging bug that only showed on a real run: `execute_remote_script` stopped reading as soon as the exit status was ready and nothing looked buffered, but the exit status can arrive before the last output chunks — so the tail of Phase 2 and the last 11 `verify.sh` checks, including its results line, were simply missing from the log of an otherwise successful provision ([bb81c01](https://github.com/carlok/portcullis/commit/bb81c01)).

The fix reads until `recv()` returns EOF and logs the remainder line by line, so the hardening record is saved in full rather than cut at the moment the process happened to exit. `tests/test_provision.py` grew the case that reproduces the split — status first, output after — next to the existing script-execution tests.
