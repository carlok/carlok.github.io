---
title: "ots-explain is public: every hop from a file to a Bitcoin block, checked by two independent implementations of one spec"
date: 2026-11-08
tags: [tool, github]
---

[ots-explain](https://github.com/carlok/ots-explain) is now public: open a `.ots` proof and see every hop from your file to a Bitcoin block, or stamp a file and upgrade the proof later, with the file never leaving the machine. Two independent implementations of one written spec have to print byte-identical reports — a single static page (81 KB, no dependencies, runs from `file://`) and a stdlib-only Python script — over five steps: your file against the digest the proof names, the proof parsed with strict limits, every hash operation recomputed, the ledger only on request, and a verdict that is green only when every check passed and none was skipped.

The page does the stamping half too: it hashes in the tab, shows the exact requests before making them, sends only `SHA-256(digest ‖ 16 random bytes)` to the public calendars, and upgrades the pending proof when you come back; the script's `watch` mode does the same from cron or a systemd timer. A real stamp from 8 November is checked in the page against two Esplora explorers, blockstream.info and mempool.space, and proved against block 975064. `./podman.sh` runs the tests, the build, the CLI and the REST API in containers, and the README records the one honest browser limit: a calendar's "not confirmed yet" answer carries no CORS header, so a pending proof reads as unreachable in the page while the script has no such restriction ([c2d1fb5](https://github.com/carlok/ots-explain/commit/c2d1fb5), [904f65a](https://github.com/carlok/ots-explain/commit/904f65a)).
