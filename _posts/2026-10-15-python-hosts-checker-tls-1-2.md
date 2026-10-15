---
title: "python-hosts-checker: the certificate check asks for TLS 1.2 at least"
date: 2026-10-15
tags: [security, tool]
---

[python-hosts-checker](https://github.com/carlok/python-hosts-checker) — the AWS Lambda endpoint and certificate monitor whose findings arrive as Telegram alerts — now sets an explicit `minimum_version` of TLS 1.2 on the `SSLContext` it uses for the expiry handshake, so TLSv1 and TLSv1.1 can never be negotiated whatever the interpreter and OpenSSL defaults happen to be ([e853782](https://github.com/carlok/python-hosts-checker/commit/e853782), [#6](https://github.com/carlok/python-hosts-checker/pull/6)). Python 3.10 and later already default `create_default_context()` to TLS 1.2, so nothing changes in practice; the floor becomes explicit instead of inherited, and it clears the CodeQL finding [code-scanning #1](https://github.com/carlok/python-hosts-checker/security/code-scanning/1) (`py/insecure-protocol`). A test captures the context handed to the handshake and asserts the floor rather than trusting the default, and the suite stands at 15 passing.
