---
title: "JPA: an HTTP failure is logged through Android's own channel"
date: 2026-10-24
tags: [project]
---

[JPA](https://github.com/carlok/JPA) — *JSON Partners Agenda*, an Android app
from 2010 that reads a JSON agenda from a URL — had `MyHttpClient` print its
stack trace straight to the process's error stream when a request failed. The
one-file fix on the `daily-care/2026-10-24-http-error-logging` branch sends it
to `Log.e` instead, under a stable tag, so a failure shows up in `logcat` with
the rest of the app's output rather than as an unattributed trace
([11bf7af](https://github.com/carlok/JPA/commit/11bf7af)).

The repository's `main` branch last moved in December 2010; this is a
maintenance commit on a branch, not a revival of the app.
