---
title: "pacenotch: the daily update check is on by default, and the notice links the build that matches your machine"
date: 2026-10-30
tags: [tool, security]
---

[pacenotch](https://github.com/carlok/pacenotch) now checks for a newer release once a day on new installs, through `DefaultSettings` rather than a change to anyone's saved configuration ([ed93612](https://github.com/carlok/pacenotch/commit/ed93612), [#3](https://github.com/carlok/pacenotch/pull/3)). The notice is the part worth reading: `internal/update` parses the release's assets, matches the GUI build for the current `GOOS`/`GOARCH` by prefix and falls back to the release page when nothing matches, so the tray and the About window can offer a download action and the release notes instead of a link to a page where the reader picks their own binary.

The same day's second pull request takes the `go` directive in `go.mod` from `1.27` to `1.27.3` for the standard library's security fixes ([47616a3](https://github.com/carlok/pacenotch/commit/47616a3), [#2](https://github.com/carlok/pacenotch/pull/2)). Both changes come with tests — the asset-matching and the settings default are covered in `internal/update/update_test.go` and `internal/gui/ui_fyne_test.go`.
