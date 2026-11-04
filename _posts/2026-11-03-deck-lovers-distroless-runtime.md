---
title: "deck-lovers moves its server runtime to Distroless, with a healthcheck that needs no shell"
date: 2026-11-03
tags: [podman, tool]
---

[deck-lovers](https://github.com/carlok/deck-lovers) now builds its server in two stages: `python:3.11-slim-bookworm` for the dependencies and `gcr.io/distroless/python3-debian12:nonroot` for the runtime, with the builder pinned to bookworm so its glibc matches the runtime's ([#6](https://github.com/carlok/deck-lovers/pull/6), [4c22adb](https://github.com/carlok/deck-lovers/commit/4c22adb)). The catch was Python's own path: Debian's `/usr/bin/python3` searches only `dist-packages`, so the packages pip installed with `--prefix /usr/local` were not importable and the container exited on `No module named uvicorn` until `PYTHONPATH` was set.

With no shell and no curl in the image, the healthcheck became code: `server.py` gained a `healthcheck` subcommand, and both the Dockerfile and `docker-compose.yml` call `/usr/bin/python3` explicitly because an exec-form healthcheck ignores `ENTRYPOINT`. The README drops the `podman debug` / `docker debug` advice, which never existed, for guidance that works: `podman-compose` 1.5 or newer for the exec-form check and the `--format docker` caveat when a Dockerfile `HEALTHCHECK` is used.
