---
title: "parsimagma: concept DOIs in the badge, version DOIs in the paper, no working directory in the proof logs"
date: 2026-09-01
tags: [math, research]
---

[parsimagma](https://github.com/carlok/parsimagma)'s citation surface was
settled deliberately: the README badge and posts cite the concept DOI
[10.5281/zenodo.22237100](https://doi.org/10.5281/zenodo.22237100), which always
resolves to the newest release, while the paper's bibliography keeps the version
DOI, because
[a report of measurements should pin the artifact it measured](https://github.com/carlok/parsimagma/commit/e9a27b3)
— and the write-up DOI was repointed at the current version rather than the one
carrying a superseded-version banner
([16d60e0](https://github.com/carlok/parsimagma/commit/16d60e0)). The same pass
took the working directory out of the published Vampire logs: the proofs are
worth publishing, the absolute temp path they were produced under is not
([2f9bf2d](https://github.com/carlok/parsimagma/commit/2f9bf2d)).
