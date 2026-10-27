---
title: "aristowrap moves to Python 3.15, and CI follows the image instead of trailing it"
date: 2026-10-26
tags: [lean4, tool]
---

[aristowrap](https://github.com/carlok/aristowrap) now builds from `python:3.15-slim-bookworm` and tests 3.15 in CI ([#11](https://github.com/carlok/aristowrap/pull/11), [a81a665](https://github.com/carlok/aristowrap/commit/a81a665)). Dependabot had already opened the base-image bump on its own, but the workflow matrix still covered only 3.11–3.14, so the change that landed applies the image and extends the matrix, the `Programming Language :: Python :: 3.15` classifier and the docs in one commit — `requires-python` stays at `>=3.11`.

Nothing in the wrapper had to change: `uv run --python 3.15 pytest` gives 47 passed at 100% coverage on `scripts.aristowrap.py`, the image reports CPython 3.15.1, the CLI loads and `lake build` succeeds in the image step, and every dev dependency resolves from wheels. Ruff went to 0.17.2 the same day ([#10](https://github.com/carlok/aristowrap/pull/10)).
