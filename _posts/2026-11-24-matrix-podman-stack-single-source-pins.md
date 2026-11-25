---
title: "matrix-podman-stack: one owner for exact pins, and a test that keeps Dependabot's bumps resolvable"
date: 2026-11-24
tags: [podman, project]
---

The CI job in [matrix-podman-stack](https://github.com/carlok/matrix-podman-stack) installs three requirement files in one pip resolution, and two of them exact-pinned `nats-py`: `requirements-dev.txt` and the example bot's own file. So when Dependabot bumped the root one, the combined resolution became impossible and the pull request could not go green — [PR #53](https://github.com/carlok/matrix-podman-stack/pull/53) failed exactly that way ([#54](https://github.com/carlok/matrix-podman-stack/pull/54), [c1d5c03](https://github.com/carlok/matrix-podman-stack/commit/c1d5c03)).

The fix is ownership rather than a looser pin: the example bot's file declares lower bounds only, `requirements-dev.txt` stays the single owner of exact versions, and [`tests/test_requirements_single_source.py`](https://github.com/carlok/matrix-podman-stack/blob/main/tests/test_requirements_single_source.py) fails if a package is pinned twice, if a non-owning file pins at all, or if a declared package has no version owner — so the next bump cannot reintroduce the conflict silently.

The same day the stack took the bumps that PR was blocking: `qdrant/qdrant` to v1.20.2, `valkey/valkey` to 9.2.0-alpine, `library/nats` to 2.15.3-alpine, `boto3` to 1.44.8 and `nats-py` to 2.17.0 ([#49](https://github.com/carlok/matrix-podman-stack/pull/49)–[#53](https://github.com/carlok/matrix-podman-stack/pull/53)).
