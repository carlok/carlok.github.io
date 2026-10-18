---
title: "roundstorm: a trimmed transcript leaves one line per dropped message"
date: 2026-10-17
tags: [tool]
---

The transcript cap in [roundstorm](https://github.com/carlok/roundstorm) used to cut silently: once the history budget bound, the oldest messages were simply gone. [#61](https://github.com/carlok/roundstorm/pull/61) now leaves one line per dropped message — `- Alice, round 2 [object]: first sentence...`, 140 characters at most, inside a 6,000-character or 15%-of-budget allowance whichever is smaller, newest lines first ([866e3f5](https://github.com/carlok/roundstorm/commit/866e3f5)). There is no model call in it, so no added cost or latency, and the trade the note on the pull request names is that a first sentence is a crude gist. A simulated run of five agents over twelve rounds puts total prompt volume 22% below uncapped, 18% with the bare marker alone, with each turn bounded — but it is still not measured on a real five-by-five, which [issue #33](https://github.com/carlok/roundstorm/issues/33) asks for, so the pull request says Refs rather than Closes.
