---
title: "forgepulse: a restart no longer leaves a sync run marked as still running"
date: 2026-10-15
tags: [rust, tool]
---

[forgepulse](https://github.com/carlok/forgepulse)'s sync-run history could not survive its own deployment: a sync interrupted by a restart stayed `running` for good, so the table advertised a job that had neither finished nor failed. A new `fail_interrupted_sync_runs()` runs at startup, marks every such row failed with `interrupted by restart` and a finish time, and the test that covers it also asserts that finished runs are left alone and that a second call is a no-op ([13e081c](https://github.com/carlok/forgepulse/commit/13e081c)). The same round added browser tests for the parts unit tests cannot see — the award badge, the fleet-wide stars feed and the sidebar breakpoint ([1f67aea](https://github.com/carlok/forgepulse/commit/1f67aea)) — a one-command local deploy script with a README line ([272af74](https://github.com/carlok/forgepulse/commit/272af74)), and a transitive `devalue` bumped to 5.9.4 to clear six Dependabot alerts ([cc8b94a](https://github.com/carlok/forgepulse/commit/cc8b94a)).
