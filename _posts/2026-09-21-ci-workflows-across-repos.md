---
title: "CI workflows land across seven repositories"
date: 2026-09-21
tags: [github, tool]
---

Seven repositories that had no continuous integration now run their own tests on
every push: [topshift-trend](https://github.com/carlok/topshift-trend/commit/53181c7)
(running `ruff` and `pytest`), [caciarabot](https://github.com/carlok/caciarabot/commit/b8052fb)
and [python-hosts-checker](https://github.com/carlok/python-hosts-checker/commit/07f9287)
(`pytest`), [euclean](https://github.com/carlok/euclean/commit/0d9e469) (`pytest`
together with its Lean build), and [quadratula](https://github.com/carlok/quadratula/commit/f688552),
[unstated-conclusions](https://github.com/carlok/unstated-conclusions/commit/422bed5)
and [prove2me-logs](https://github.com/carlok/prove2me-logs/commit/32e455a) with
smoke tests — in prove2me-logs' case covering the `p2m` helper, the piece the
mission journal is actually read through.

None of these were failing before; they simply had nothing watching them, which
is the state a test suite quietly returns to. The two verified-math repositories
in the sweep ([magma-1518-obstruction-lean](https://github.com/carlok/magma-1518-obstruction-lean/commit/b77644e),
[erdos-straus-offset-lean](https://github.com/carlok/erdos-straus-offset-lean/commit/aa79d27))
got axiom audits in the same pass.
