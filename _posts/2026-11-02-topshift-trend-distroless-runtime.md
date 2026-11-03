---
title: "topshift-trend moves production to Distroless Python, and the venv had to be built by the right python"
date: 2026-11-02
tags: [bot, podman]
---

[topshift-trend](https://github.com/carlok/topshift-trend) now builds its production image on `gcr.io/distroless/python3-debian12:nonroot` in a multi-stage Containerfile, with the virtualenv built on `python:3.11-slim-bookworm` to match the Distroless interpreter and `requires-python` relaxed to `>=3.11` for it ([#11](https://github.com/carlok/topshift-trend/pull/11), [ead6607](https://github.com/carlok/topshift-trend/commit/ead6607)).

The catch was the interpreter, not the base image. Creating the venv with a plain `python3` resolved to `/usr/local/bin`, which does not exist in Distroless, so the container died on `executable file /app/.venv/bin/python3 not found`; building it through `/usr/bin/python3` points the symlink and `pyvenv.cfg`'s home at the path the runtime actually has. The image runs as UID 65532, so `compose.yaml` drops the `user: PUID:PGID` override, `.env.example` drops the two variables, and the README now says to chown `./data` to 65532 — `podman unshare chown` for rootless, `sudo chown` for rootful — replacing a `podman debug`/`docker debug` section that never existed with host-side inspection tips. The compose build is pinned to the runtime target.
