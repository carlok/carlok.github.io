# carlok.github.io

GitHub Pages source for [carlok.github.io](https://carlok.github.io/), the
GitHub-facing project atlas, research-notes hub, and public activity log for
Carlo Perassi.

## Structure

- `_layouts/` — custom Jekyll layouts (`default`, `post`)
- `assets/css/main.css` — the design system (light, technical, Vercel/Linear inspired)
- `index.md`, `projects.md`, `writing.md`, `blog.md` — the four pages
- `_posts/` — blog entries (one markdown file per entry)

## Notes

- **LeanFrontier is a separate site.** It lives at
  [github.com/carlok/LeanFrontier](https://github.com/carlok/LeanFrontier) and is
  deployed independently to [carlok.github.io/LeanFrontier/](https://carlok.github.io/LeanFrontier/).
  This repo only links to it.
- **The blog is updated by a daily cron** that checks public GitHub activity,
  writes a new `_posts/` entry when something important changes, and pushes.
