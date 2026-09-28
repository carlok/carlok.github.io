---
title: "pacenotch fingerprints credentials by expiry instead of hashing the token"
date: 2026-09-28
tags: [tool, security]
---

[pacenotch](https://github.com/carlok/pacenotch) notices that Claude Code has
refreshed its OAuth token by fingerprinting the credentials it reads, and that
fingerprint used to be a SHA-256 of the access token — which CodeQL flagged as
`go/weak-sensitive-data-hashing`
([a63ee1f](https://github.com/carlok/pacenotch/commit/a63ee1f)). The hash never
left memory, but hashing the secret was never needed to detect a refresh: the
fingerprint is now `claudeAiOauth.expiresAt`, a value every refresh moves and
which is not secret at all, while a `PACENOTCH_TOKEN` cannot change while the
program runs and gets a fixed fingerprint. It is the second CodeQL-driven
correction in pacenotch's credential layer after the recovery path stopped
re-reading the token.
