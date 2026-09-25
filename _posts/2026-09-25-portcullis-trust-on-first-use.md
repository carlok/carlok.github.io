---
title: "portcullis: Phase 1 stops accepting any SSH host key"
date: 2026-09-25
tags: [security, tool]
---

[portcullis](https://github.com/carlok/portcullis) replaced paramiko's
`AutoAddPolicy` — which accepts whatever key a host presents — with an explicit
trust-on-first-use policy ([25da71b](https://github.com/carlok/portcullis/commit/25da71b)).
Phase 1 is the first contact with a VM created seconds earlier by the same
process, so there is no prior key to compare against and Hetzner does not
publish the fingerprint through its API: the new policy accepts that first key
once, logs its type and fingerprint, and Phase 2 still connects with that exact
key pinned, so a later substitution is detected. The change addresses CodeQL's
`py/paramiko-missing-host-key-validation` alert, and the test that asserted the
blanket policy now asserts the new one. The [secret-handling pass of 21
September](/blog/2026/09/21/portcullis-secrets/) had already pinned the key Phase
2 connects with; the first contact was still an unconditional accept.
