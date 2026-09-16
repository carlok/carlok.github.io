---
title: "pacenotch: a Settings window, start at login, and one instance at a time"
date: 2026-09-15
tags: [tool, project]
---

[pacenotch](https://github.com/carlok/pacenotch)'s GUI grew the controls a
`.app` cannot be handed on the command line: a **Settings** window (footer
button, tray menu, *pacenotch → Settings…* on macOS) for the on-pace band,
the refresh interval, notifications, compact mode, appearance and Dock
behaviour, applied and saved as they change
([13dc75f](https://github.com/carlok/pacenotch/commit/13dc75f)). Because a
MacBook's camera notch can hide the menu bar icon and with it the only Quit,
the app can now switch to the Regular activation policy and live in the Dock
and Cmd-Tab with a Quit in the window and a Settings window that is not hidden
by the notch ([b6f4031](https://github.com/carlok/pacenotch/commit/b6f4031)).

Only one GUI runs at a time — the first listens on a unix socket in the user
cache and a second launch, from a terminal, a login item or the app itself,
hands over instead of opening a duplicate tray icon
([cd848f5](https://github.com/carlok/pacenotch/commit/cd848f5)) — and *start at
login* writes the operating system's own login entry for the running copy, so
the setting can never disagree with what actually starts
([84f4fdf](https://github.com/carlok/pacenotch/commit/84f4fdf)). An expired
token is now refreshed through Claude Code, which refreshes its OAuth token
only when it makes a request: pacenotch runs one tiny restricted request on the
smallest model (verified by hand — `claude auth status` does not refresh, a
headless `claude -p` does), at most every ten minutes after a 401, and while
authentication keeps failing it answers from memory rather than calling the
endpoint every minute
([393f134](https://github.com/carlok/pacenotch/commit/393f134)). An opt-in,
off-by-default daily check reads GitHub's latest-release API — tag and page
address only, 1 MiB cap, drafts and pre-releases ignored — and reports a newer
release in the tray and About window without downloading anything
([7a925ae](https://github.com/carlok/pacenotch/commit/7a925ae)). One Windows
test fix rode along: `filepath.Dir` follows the host OS, so the fake macOS
path's directory is `\usr\local\bin` there, and the expected PATH was
hard-coded in the Unix form ([8765882](https://github.com/carlok/pacenotch/commit/8765882)).
