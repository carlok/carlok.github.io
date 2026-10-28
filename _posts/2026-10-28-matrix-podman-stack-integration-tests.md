---
title: "matrix-podman-stack: an integration suite that runs the real stack, and pip-audit in CI"
date: 2026-10-28
tags: [podman, project, security]
---

[matrix-podman-stack](https://github.com/carlok/matrix-podman-stack) grew the layer the unit tests could not reach. [docs/testing-plan.md](https://github.com/carlok/matrix-podman-stack/blob/main/docs/testing-plan.md) inventories the gaps, and the new suite closes them by running the actual containers: a Postgres 16→18 migration checked end to end through `/health` and through Matrix users, a room and messages that survive it, a Garage in-place upgrade driven with `boto3`, the NATS/Valkey bus hooks, and the monitoring profile including the Grafana datasource proxy query ([#27](https://github.com/carlok/matrix-podman-stack/pull/27), [1148def](https://github.com/carlok/matrix-podman-stack/commit/1148def)).

The fixtures are what made it runnable: `compose_stack.sh` and `podman-compose` drive the stack on GitHub Actions, `HOST_UID`/`HOST_GID` keep the bootstrap writing as the right user in CI, and the Telegram bridge is set up the way an operator would — the example config first, then `-g` — after three false starts on the binary path, the Element config assertion and the Grafana 13 proxy URL ([1964e57](https://github.com/carlok/matrix-podman-stack/commit/1964e57), [288f1b1](https://github.com/carlok/matrix-podman-stack/commit/288f1b1), [393970f](https://github.com/carlok/matrix-podman-stack/commit/393970f)).

That day's second pull request closes a gap `docs/SECURITY-AUDIT.md` had admitted: CI ran pytest and ruff only, leaving PyPI advisories to a human. `pip-audit` now scans `requirements-dev.txt`, `scripts/requirements.txt` and `bots/example_bot/requirements.txt` in the lint job, and the duplicate bot-only Ruff step went, since the consolidated check already covers `bots/` ([#28](https://github.com/carlok/matrix-podman-stack/pull/28), [1fa915e](https://github.com/carlok/matrix-podman-stack/commit/1fa915e)). Unit coverage stands at 95.75% with the integration marker excluded.
