---
title: "forgepulse: self-hosted GitHub traffic-history analytics"
date: 2026-08-24
tags: [rust, tool, podman]
---

[forgepulse](https://github.com/carlok/forgepulse) is now public: a self-hosted
GitHub traffic-history analytics app built with Rust, a Svelte frontend, SQLite
for storage, and Podman for deployment. It keeps a running history of GitHub
traffic metrics so trends accumulate instead of vanishing after GitHub's
rolling window.
