---
title: "contributed to pyasn1 and python-multipart: three ordering and chunking bugs"
date: 2026-10-21
tags: [contribution, tool]
---

Three pull requests went upstream on 2026-10-21, each with a failing test first. On [pyasn1/pyasn1](https://github.com/pyasn1/pyasn1), [BitString ordering](https://github.com/pyasn1/pyasn1/pull/130) breaks on equal-length values: `__lt__` and `__gt__` compare length then value, but `__le__` and `__ge__` test `len(a) <= len(b) or ...`, already true when the lengths match, so the value is never reached — `BitString(binValue='11') <= BitString(binValue='10')` and the same pair with `>` both come back true. Comparing lengths strictly in the two operators fixes it, two tests go in and the suite moves from 1261 to 1263.

On [Kludex/python-multipart](https://github.com/Kludex/python-multipart), [QuotedPrintableDecoder](https://github.com/Kludex/python-multipart/pull/344) made a decoded upload depend on where the caller's reads fell: `write()` kept the last two bytes for the next call whenever they contained `=`, so a chunk ending `=41=` held back `1=` and decoded `=4` as literal text — `b'=41='` then `b'42'` gave `=41B` where one write gives `AB`. Keeping only the bytes from the last `=` within the final two decodes a complete escape at once and leaves just an unfinished one (`=`, `=4`) waiting; a test over every two-way split of four inputs fails four ways before the fix, and the suite goes from 163 to 167.

The third, [a nameless upload](https://github.com/Kludex/python-multipart/pull/343), is the TODO the parser had been carrying: `File.__init__` sets `_file_base` and `_ext` only when it is given a filename, so an `application/octet-stream` part created with `file_name=None` that passes `MAX_MEMORY_FILE_SIZE` hits `AttributeError` in `_get_disk_file` as soon as `UPLOAD_KEEP_EXTENSIONS` or `UPLOAD_KEEP_FILENAME` is on. Without a filename the two attributes now default to `None` and empty and the file falls back to a temporary file in `UPLOAD_DIR`; two tests, 163 to 165. All three are open and LLM-assisted, as the [kissat report](/blog/2026/10/15/kissat-parse-line-number/) was.
