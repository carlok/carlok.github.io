---
title: "platosdf: the Flask engine API closes eleven CodeQL findings without trusting a filename"
date: 2026-10-20
tags: [security, tool]
---

[platosdf](https://github.com/carlok/platosdf), the genetic evolver for invariant signed-distance-field solids, cleared its CodeQL backlog in the Python engine that serves grammars, meshes and the gallery. The GitHub API for alert details answered 403, so the findings were reproduced locally with CodeQL CLI 2.27.2 on the `python-security-extended` and `javascript-security-extended` suites, which is what the repo's dynamic workflow runs anyway: eleven Python findings, among them `py/flask-debug` for the `debug=True` in `__main__`, `py/path-injection` twice — a user-supplied grammar `name` joined onto a path in `engine/grammar_store.py`, and the `epoch`/`filename` pair in `gallery_file` — and `py/stack-trace-exposure` on the JSON error bodies ([9158692](https://github.com/carlok/platosdf/commit/9158692), [#1](https://github.com/carlok/platosdf/pull/1)).

The fixes remove the sink rather than sanitise it. Grammar names resolve through a `glob` index of the grammar directory, so a name that is not a key of that index is simply missing; gallery epochs are matched against the actual child directories of the gallery (bounded to 0–9999) and filenames must fullmatch `^[A-Za-z0-9][A-Za-z0-9_.-]*\.(glb|json)$` before the file is looked up in a listing of that directory, which also turns a missing epoch from a 404 on a non-existent path into a 404 on a checked one. Error responses carry `Grammar not found` and `Invalid grammar payload` with no exception text, and debug mode now needs `FLASK_DEBUG` to be `1`, `true` or `yes`, so the compose setup behaves as before while a bare `python server.py` does not expose the debugger.

Re-measured locally, both suites report zero findings, down from eleven, and new tests pin the traversal rejection (`../secret`, `..`, `foo/bar`, `.hidden`) and the invalid-gallery-filename 400 ([af325da](https://github.com/carlok/platosdf/commit/af325da)).
