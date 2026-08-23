#!/usr/bin/env python3
"""Reorder projects.md: within each category, newest-pushed repo first;
categories themselves ordered by their newest item. Items whose date
can't be determined (non-GitHub links, deleted/private repos) keep
their existing relative position at the end of their category, and a
category with no dated items at all keeps its existing relative
position at the end of the page.

Run with GITHUB_TOKEN set (or --token) to avoid the 60 req/hour
unauthenticated GitHub API limit.
"""
import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

PROJECTS_MD = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "projects.md")

SECTION_RE = re.compile(r"^## (.+)$")
ITEM_LINK_RE = re.compile(r"\]\(([^)]+)\)")

GITHUB_REPO_RE = re.compile(r"^https://github\.com/([^/]+)/([^/]+?)/?(?:/.*)?$")
GITHUB_PAGES_RE = re.compile(r"^https://([^.]+)\.github\.io/([^/]+)/?.*$")


def extract_owner_repo(url):
    m = GITHUB_REPO_RE.match(url)
    if m:
        return m.group(1), m.group(2)
    m = GITHUB_PAGES_RE.match(url)
    if m:
        return m.group(1), m.group(2)
    return None


def fetch_pushed_at(owner, repo, token, cache):
    key = f"{owner}/{repo}"
    if key in cache:
        return cache[key]
    req = urllib.request.Request(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "sort-projects-script",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.load(resp)
            pushed_at = data.get("pushed_at")
            cache[key] = pushed_at
            return pushed_at
    except urllib.error.HTTPError as e:
        print(f"  warn: {key} -> HTTP {e.code}, skipping (no date)", file=sys.stderr)
        cache[key] = None
        return None
    except urllib.error.URLError as e:
        print(f"  warn: {key} -> {e}, skipping (no date)", file=sys.stderr)
        cache[key] = None
        return None


def parse_sections(text):
    """Split into (preamble, [(heading, [item_lines])])."""
    lines = text.split("\n")
    preamble = []
    sections = []
    current_heading = None
    current_items = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = SECTION_RE.match(line)
        if m:
            if current_heading is not None:
                sections.append((current_heading, current_items))
            current_heading = m.group(1)
            current_items = []
        elif current_heading is not None:
            if line.strip().startswith("-"):
                current_items.append(line)
        else:
            preamble.append(line)
        i += 1
    if current_heading is not None:
        sections.append((current_heading, current_items))
    return preamble, sections


def sort_items(items, token, cache):
    dated = []
    undated = []
    for idx, line in enumerate(items):
        m = ITEM_LINK_RE.search(line)
        date = None
        if m:
            owner_repo = extract_owner_repo(m.group(1))
            if owner_repo:
                date = fetch_pushed_at(*owner_repo, token=token, cache=cache)
        if date:
            dated.append((date, line))
        else:
            undated.append((idx, line))
    dated.sort(key=lambda t: t[0], reverse=True)
    sorted_lines = [line for _, line in dated] + [line for _, line in undated]
    max_date = dated[0][0] if dated else None
    return sorted_lines, max_date


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN"))
    parser.add_argument("--check", action="store_true", help="exit 1 if file would change, without writing")
    args = parser.parse_args()

    with open(PROJECTS_MD, encoding="utf-8") as f:
        original = f.read()

    preamble, sections = parse_sections(original)
    cache = {}

    resolved = []
    for heading, items in sections:
        sorted_items, max_date = sort_items(items, args.token, cache)
        resolved.append((heading, sorted_items, max_date))

    dated_sections = [s for s in resolved if s[2]]
    undated_sections = [s for s in resolved if not s[2]]
    dated_sections.sort(key=lambda s: s[2], reverse=True)
    ordered = dated_sections + undated_sections

    out_lines = list(preamble)
    for heading, items, _ in ordered:
        out_lines.append(f"## {heading}")
        out_lines.append("")
        out_lines.extend(items)
        out_lines.append("")
    while out_lines and out_lines[-1] == "":
        out_lines.pop()
    new_text = "\n".join(out_lines) + "\n"

    if new_text == original:
        print("projects.md already sorted, no changes.")
        return 0

    if args.check:
        print("projects.md is out of date.")
        return 1

    with open(PROJECTS_MD, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("projects.md reordered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
