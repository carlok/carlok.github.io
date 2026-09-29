---
title: "Contributed to PalomarRegistry/PalomarSubmission: registration stopped creating archive copies"
date: 2026-09-28
tags: [contribution, lean4, github]
---

Contributed [PalomarRegistry/PalomarSubmission#156](https://github.com/PalomarRegistry/PalomarSubmission/issues/156):
registration of an accepted submission had been "under way" for more than seven
hours, the status page's last event being `2026-09-28T08:09:00Z — The submitter
asked for this result to be registered`, with no `palomar/…` tag on the
repository and no `PalomarArchive` copy created. The issue reports that this is
not local to one submission: the newest repository in the `PalomarArchive`
organisation was created at `06:50Z` and none since, for anyone, while the rest
of the pipeline looked healthy — 24 workflow runs started in `PalomarSubmission`
since `09:00Z`, 20 of them successful.

The submission in question is
[magma-1518-obstruction-lean](https://github.com/carlok/magma-1518-obstruction-lean)
at commit
[`eb2bbde`](https://github.com/carlok/magma-1518-obstruction-lean/commit/eb2bbde),
whose mechanical verification passed, whose `Challenge` render succeeded and for
which the automated review offered registration. The issue asks whether
registration is paused or whether that submission is waiting on a step from the
submitter, since verification, rendering and review appear sound while
registration and source preservation do not advance.
