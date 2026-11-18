---
title: "slop-audit: nltk and setuptools pinned against two advisories, and a CI workflow that does not run the installer"
date: 2026-11-08
tags: [security, tool]
---

The slop environment in [slop-audit](https://github.com/carlok/slop-audit) now pins `nltk>=3.10.4` and `setuptools>=84.1.0` inside `install_slop_env`, before the freeze is written, to clear PYSEC-2026-3740 and GHSA-xmj3-9gf7-h52w — with `logs/pip_freeze_slop.txt` regenerated from a full install run rather than edited by hand ([8b50ad0](https://github.com/carlok/slop-audit/commit/8b50ad0), [#4](https://github.com/carlok/slop-audit/pull/4)). The same commit adds a CI workflow that runs basic `pytest` and a syntax check of the install script on push and pull request under read-only `contents`, and deliberately does not execute `install_all.sh` or provision the external toolchains it would pull down. That is the right boundary for a repository whose setup script is the thing under test.
