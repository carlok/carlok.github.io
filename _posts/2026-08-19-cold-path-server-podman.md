---
title: "cold-path-server-podman: the Cold Path game server in a container"
date: 2026-08-19
tags: [podman, games, project]
---

[cold-path-server-podman](https://github.com/carlok/cold-path-server-podman) is a
new repository that runs the [Cold Path](https://github.com/jalhund/cold-path-server)
multiplayer game server inside a Podman container, so no LuaJIT, LuaSocket, or
LuaSec install is needed on the host. The upstream sources aren't vendored —
the image build pulls them from GitHub, and `make build` / `make run` / `make logs`
handle the rest.
