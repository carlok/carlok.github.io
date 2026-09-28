---
title: "pickmydegree stops tracking its own generated coverage reports"
date: 2026-09-28
tags: [security, github]
---

[pickmydegree](https://github.com/carlok/pickmydegree) had been committing the
HTML output of its test-coverage run, and CodeQL flagged the Istanbul report's
`sorter.js` assets as `js/xss-through-dom` inside that generated output
([11e72fc](https://github.com/carlok/pickmydegree/commit/11e72fc)). Those files
are test artifacts rather than application code, so `coverage/` is now ignored
and the committed reports left the tree — roughly 22,800 lines of generated HTML
and CSS removed and three added, merged as
[PR #2](https://github.com/carlok/pickmydegree/pull/2). The app source is
untouched; only the repository stops carrying a copy of its own coverage run.
