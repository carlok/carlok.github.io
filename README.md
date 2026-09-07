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

- **Prove2Me activity lives in its own repo.**
  [prove2me-logs](https://github.com/carlok/prove2me-logs) carries one entry per
  stable result, with theorem uuids, the Lean environment and what remains open.
  Posts here are written from that repo by the daily task in
  `scripts/PROVE2ME_BLOG_TASK.md`, which reads only public URLs — no API key, no
  polling, no state kept here. Those posts carry the `prove2me` tag.
