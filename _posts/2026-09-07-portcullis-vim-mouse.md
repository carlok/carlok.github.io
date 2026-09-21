---
title: "portcullis: Vim stops stealing the terminal's mouse selection"
date: 2026-09-07
tags: [security, tool]
---

[portcullis](https://github.com/carlok/portcullis) hardens a fresh Ubuntu host,
and hardening has to leave the machine pleasant to actually use: Ubuntu's Vim
defaults enable xterm mouse reporting, so on a remote terminal Vim captures the
selection and ordinary copy/paste stops working. A new Phase 2 section,
`1.6a — Terminal editor defaults`, now
[ships `/etc/vim/vimrc.local`](https://github.com/carlok/portcullis/commit/8c358de4644f96c570679cbcf90bc47d90b56b61)
with `set mouse=` (and a note in the README's Phase 2 list), leaving selection to
the terminal emulator while anyone who wants Vim's mouse support can opt back in.

The placement is the point: Vim sources `vimrc.local` *before* its own
`defaults.vim`, so doing it there alone would have been overwritten. The override
is deferred to a `VimEnter` autocmd inside a dedicated augroup instead, and the
same commit adds the repository's first Phase 2 test,
[`tests/test_phase2_defaults.py`](https://github.com/carlok/portcullis/blob/main/tests/test_phase2_defaults.py),
which asserts both the `vimrc.local` write and the deferred `VimEnter` line so
the fix cannot silently regress.
