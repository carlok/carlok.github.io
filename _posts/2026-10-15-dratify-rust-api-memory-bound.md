---
title: "dratify: the Rust checker's memory bound is written down, and Python 3.15 is declared"
date: 2026-10-15
tags: [security, tool]
---

Two gaps closed in [dratify](https://github.com/carlok/dratify), the in-process DRAT/DRUP proof checker. The Python layer has bounded its literal widths since 0.1.7, but a Rust caller handed an untrusted literal near `u32::MAX` makes the checker ask for roughly 200 GB and abort — a real property of the API that appeared nowhere in its documentation, so `Checker` now says so and names the bound the Python layer applies ([85ddd58](https://github.com/carlok/dratify/commit/85ddd58)). The package also declares the Python 3.15 classifier, 3.15.0 being final and CI having tested it since the release candidates; it stays on `main` until the next release rather than warranting a version of its own ([f4f1ccb](https://github.com/carlok/dratify/commit/f4f1ccb)).
