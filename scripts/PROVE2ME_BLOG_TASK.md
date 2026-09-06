# Task: Prove2Me → blog

Run this daily (suggested 06:30 local, just before the 06:17 UTC `sort-projects` Action).
Self-contained: everything needed is below.

**Repo:** `/Users/carlo/Documents/varie/hacks/github/carlok.github.io` — Jekyll, branch `main`, remote `origin`.

---

## 1. Poll

```bash
cd /Users/carlo/Documents/varie/hacks/github/carlok.github.io
git pull --rebase
python3 scripts/prove2me_activity.py
```

The script prints either `prove2me: no changes` or a digest of what changed since the last run.

It reads the API key from `$PROVE2ME_KEY`, falling back to the `prove2me_key=` line of
`/Users/carlo/Documents/varie/hacks/lean4/prove2me/.env`. **Never print, log, commit, or
transmit that key.** It must not appear in a post, a commit message, or
`_data/prove2me_state.json` (the script already keeps it out of the state file).

If the output is `prove2me: no changes` — stop. Write nothing, commit nothing, push nothing.

## 2. Decide whether it earns a post

Report only substantive events:

- a theorem changing status (Open → Proved / Disproved) — always worth a post
- a submission accepted (`PROVED`, `SKETCH_ACCEPTED`)
- a new theorem published to the platform
- a meaningful trust or solved-count change

Skip: `ERROR` verdicts (server-side infrastructure faults — the script already filters these),
`PENDING`/`COMPILING` states, and vote-count jitter with nothing else attached. If everything
new is noise, stop as in step 1.

## 3. Gather substance

A post must say what was actually proved, not just that something happened. Read, in order:

1. `/Users/carlo/Documents/varie/hacks/lean4/prove2me/missions/*/NOTES.md` — the working notes,
   with the lemma chains, the mathematical detail, and what remains open
2. the theorem's natural-language statement — `GET https://prove2.me/api/v1/theorems/<id>`
3. the submission's `explanation` field — `GET https://prove2.me/api/v1/submissions/<id>`

API auth: `POST https://prove2.me/api/v1/agent/refresh` with `{"api_key": "..."}` returns a
1-hour `access_token`; send it as `Authorization: Bearer <token>`.

## 4. Write the post

Create `_posts/YYYY-MM-DD-<slug>.md` with today's date.

```yaml
---
title: "..."
date: YYYY-MM-DD
tags: [lean4, math, research, prove2me]
---
```

The `prove2me` tag is **required** on every post from this task — `tag/prove2me.md` already
exists. Keep `lean4`, `math`, `research` where they genuinely apply.

Match the voice of the existing posts in `_posts/` — read two or three recent ones first.
First person, concrete, technical, specific numbers and names. No hype, no "excited to share".
State what was proved and what is still open. Roughly 150–300 words unless the event warrants
more.

**Links.** prove2.me is an external site, so use full absolute URLs, never relative paths:

| what | URL |
|---|---|
| theorem | `https://prove2.me/theorems/<theorem_id>` |
| mission | `https://prove2.me/missions/<mission_id>` |
| submission | `https://prove2.me/submissions/<submission_id>` |
| profile | `https://prove2.me/users/<user_id>` |

These shapes are verified. The singular forms `/theorem/` and `/mission/` return 404, and
`/users/<username>` 404s too — the profile URL takes the uuid, not the name. Link both the
theorem and the submission for anything you report.

## 5. Publish

```bash
python3 scripts/prove2me_activity.py --write   # update the state file
git add _posts/<the new post> _data/prove2me_state.json
git commit -m "Post: <short description of the Prove2Me result>"
git push
```

Commit the state file in the **same commit** as the post, so a failed push cannot leave the
recorded state ahead of the published record.

If `git push` is rejected, `git pull --rebase` and push again. If it still fails, leave the
commit local and report the failure — do not force-push.

## 6. Report

Say what you published, the post filename, and the live URL:
`https://carlok.github.io/blog/YYYY/MM/DD/<title-slug>/`

---

## Current context (as of 2026-09-06)

Account `carlok`. The watchlist in `_data/prove2me_state.json` currently tracks the
[Bochner's Theorem mission](https://prove2.me/missions/477bb57a-f923-42e7-a087-2d04507a18fa):

| theorem | status |
|---|---|
| [`Bochner.bochner_theorem`](https://prove2.me/theorems/3e8cf854-ea51-4337-b240-86b51152b602) — the mission goal | Open |
| [`Bochner.bochner_L1_case`](https://prove2.me/theorems/28648a73-641e-4cb5-88e9-176299642e57) — the milestone | Open, reduced |
| [`Bochner.fourierTransform_nonneg`](https://prove2.me/theorems/5c399c24-e6b3-41f4-bdf8-bdef8ebcdbdb) | Open, reduced |
| [`Bochner.fourierTransform_integrable`](https://prove2.me/theorems/aabc90c7-0956-4ce1-8605-3350bee69304) | Open, reduced |
| [`Bochner.posDef_continuous_extension`](https://prove2.me/theorems/49b85d71-09c1-4f47-8b52-a8d07523906a) | Open — the whole frontier |

All three accepted submissions are proof sketches, so the chain resolves the moment
`posDef_continuous_extension` is proved: that one lemma closes the other three and the
milestone with it. That status change is the headline to watch for.

To follow another mission, add its theorem ids to the `watchlist` array in
`_data/prove2me_state.json`; the script picks them up on the next run.
