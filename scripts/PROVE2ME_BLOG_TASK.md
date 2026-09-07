# Task: Prove2Me → blog

Run daily, before the 06:17 UTC `sort-projects` Action.

Self-contained and path-free: every input is a public URL, and no API key
is involved. If you find yourself needing a credential, you are doing the
old version of this task — stop.

## Inputs

- Logs: <https://github.com/carlok/prove2me-logs>
- Profile: <https://prove2.me/users/fca9fd8a-84f4-46ca-8845-a4a2b665381d>
- This repo: <https://github.com/carlok/carlok.github.io> — Jekyll,
  branch `main`.

Nothing here is machine-specific. Run it from a clone of this repo on any
host; if you do not have one, clone it.

## Steps

1. `git pull --rebase`.
2. Find the newest post under `_posts/` carrying the `prove2me` tag. Note
   its date.
3. In `prove2me-logs`, read `journal.md` and collect every entry dated
   after that post. **If there are none, stop.** Write nothing, commit
   nothing.
4. Read those entries in full. Each one is the source of truth for what
   it reports. Its `## What is not proved` section is binding: do not
   state a result more confidently than the entry does.
5. Write one post, `_posts/YYYY-MM-DD-<slug>.md`:

   ```yaml
   ---
   title: "..."
   date: YYYY-MM-DD
   tags: [lean4, math, research, prove2me]
   ---
   ```

   The `prove2me` tag is required; `tag/prove2me.md` already exists.
   Roughly 250–350 words. First person, concrete, specific numbers and
   names, no hype. Read two or three recent posts first and match them.
6. Use absolute URLs. `https://prove2.me/theorems/<uuid>`,
   `https://prove2.me/submissions/<uuid>`,
   `https://prove2.me/missions/<uuid>`, `https://prove2.me/users/<uuid>`.
   The singular forms 404, and the profile URL takes the uuid rather than
   the username. Link the corresponding entry in `prove2me-logs` as well,
   so a reader can reach the full technical record.
7. Commit the post on its own and push. Do not touch `projects.md` — the
   `sort-projects` workflow owns that file's ordering.

## What not to do

- Do not poll the Prove2Me API. The logs repo exists to make that
  unnecessary, and the poller that used to live here has been removed.
- Do not report a result that has no entry in the logs. An entry is what
  makes a result stable enough to publish.
- Do not backfill missed days dishonestly. A gap is a gap.
