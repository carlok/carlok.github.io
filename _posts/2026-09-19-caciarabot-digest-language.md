---
title: "caciarabot: the digest stops posting links it cannot read"
date: 2026-09-19
tags: [bot, telegram]
---

The digest in [caciarabot](https://github.com/carlok/caciarabot) now skips
candidate links whose target page is in another language
([7fd451b](https://github.com/carlok/caciarabot/commit/7fd451b)), because
GitHub trending routinely surfaces repositories documented entirely in Chinese —
two of the fifty candidates in that day's live fetch were exactly that, and
posting one of them as the link of the day wastes the slot. The check runs in two
stages, cheapest first: the pool is filtered on the title and description the
source already returned, no extra request; only the *picked* candidate is fetched
and checked, because verifying fifty to post one would be fifty requests a day,
and a rejection drops that link and draws again, up to five times. For a GitHub
repo the check reads the raw README rather than the repo page, since github.com
serves `<html lang="en">` on every page it renders, including for repos written
entirely in Chinese; elsewhere the declared `lang` decides, falling back to an
English-stopword ratio over the visible text. Two deliberate non-rejections:
Latin-script languages pass the metadata stage (ten words of French cannot be told
from English reliably), and a page yielding no usable evidence is accepted rather
than quietly thinning the pool — and Greek is left out of the non-Latin script set
on purpose, since a lone alpha here is more likely to be mathematics than prose.
