# carlok.github.io

GitHub Pages source for [carlok.github.io](https://carlok.github.io/), the
GitHub-facing project atlas, research-notes hub, and public activity log for
Carlo Perassi.

## Structure

- `_layouts/` — custom Jekyll layouts (`default`, `post`)
- `assets/css/main.css` — the design system (terminal/mono aesthetic: `$` prompts, file-tree lists)
- `index.md`, `projects.md`, `writing.md`, `blog.md` — the four pages
- `_posts/` — blog entries (one markdown file per entry)

## Notes

- **LeanFrontier is a separate site.** It lives at
  [github.com/carlok/LeanFrontier](https://github.com/carlok/LeanFrontier) and is
  deployed independently to [carlok.github.io/LeanFrontier/](https://carlok.github.io/LeanFrontier/).
  This repo only links to it.
- **The blog is updated by a daily cron** that checks public GitHub activity,
  writes a new `_posts/` entry when something important changes, keeps the
  projects page (`projects.md`) in sync with new public repos, and pushes.

- **Prove2Me activity is tracked separately.** `scripts/prove2me_activity.py` polls
  [prove2.me](https://prove2.me) for new theorems, submissions and status changes on a
  watchlist, diffs against `_data/prove2me_state.json`, and prints what changed
  (`--write` updates the state). It reads the API key from `$PROVE2ME_KEY` or the
  `prove2me_key=` line of `$PROVE2ME_ENV`; the key never reaches the state file or the repo.
  Posts from it carry the `prove2me` tag.
