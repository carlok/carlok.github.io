#!/usr/bin/env python3
"""Poll Prove2Me for new activity and print a digest of what changed.

Reads the API key from $PROVE2ME_KEY, or from the `prove2me_key=` line of the
file named by $PROVE2ME_ENV (default: ~/Documents/varie/hacks/lean4/prove2me/.env).
The key is never printed and never written to the state file.

State lives in _data/prove2me_state.json: the last-seen snapshot plus a watchlist
of theorem ids whose status and submissions we follow.

Exit codes: 0 = digest printed (or "no changes"), 1 = could not reach the API.
"""

import json
import os
import sys
import urllib.error
import urllib.request

BASE = "https://prove2.me/api/v1"
SITE = "https://prove2.me"

# Verified URL shapes on prove2.me (all plural; the singular forms 404):
#   /theorems/<theorem_id>  /missions/<mission_id>
#   /users/<user_id>        /submissions/<submission_id>
# /users/<username> does NOT work - the profile URL takes the uuid.
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_PATH = os.path.join(ROOT, "_data", "prove2me_state.json")
DEFAULT_ENV = os.path.expanduser("~/Documents/varie/hacks/lean4/prove2me/.env")


def read_key():
    key = os.environ.get("PROVE2ME_KEY")
    if key:
        return key.strip()
    path = os.environ.get("PROVE2ME_ENV", DEFAULT_ENV)
    try:
        with open(path) as fh:
            for line in fh:
                if line.startswith("prove2me_key="):
                    return line.split("=", 1)[1].strip().strip("'\"")
    except OSError:
        pass
    sys.exit("no Prove2Me API key: set PROVE2ME_KEY or PROVE2ME_ENV")


def access_token(key):
    req = urllib.request.Request(
        f"{BASE}/agent/refresh",
        data=json.dumps({"api_key": key}).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    return json.load(urllib.request.urlopen(req, timeout=60))["access_token"]


def get(token, path):
    req = urllib.request.Request(path if path.startswith("http") else BASE + path,
                                 headers={"Authorization": "Bearer " + token})
    return json.load(urllib.request.urlopen(req, timeout=60))


def load_state():
    try:
        with open(STATE_PATH) as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {"profile": {}, "theorems": {}, "submissions": {}, "watchlist": []}


def snapshot(token, state):
    me = get(token, "/me")
    uid = me["user_id"]
    profile = get(token, f"/users/{uid}")

    watch = set(state.get("watchlist", []))
    for row in profile.get("submitted_problems", []):
        watch.add(row["theorem_id"])
    for row in profile.get("solved_problems", []):
        watch.add(row.get("theorem_id", ""))
    watch.discard("")

    theorems, submissions = {}, {}
    for tid in sorted(watch):
        try:
            t = get(token, f"/theorems/{tid}")
        except urllib.error.HTTPError:
            continue
        theorems[tid] = {"name": t["theorem_name"], "title": t["theorem_title"],
                         "status": t["status"], "votes": t.get("vote_count", 0)}
        try:
            subs = get(token, f"/theorems/{tid}/submissions").get("submissions", [])
        except urllib.error.HTTPError:
            subs = []
        for s in subs:
            if s.get("user_id") == uid or s.get("username") == me.get("username"):
                submissions[s.get("id") or s.get("submission_id", "")] = {
                    "theorem_id": tid, "theorem_name": t["theorem_name"],
                    "status": s.get("status"), "created_at": s.get("created_at"),
                }
    submissions.pop("", None)

    return uid, {
        "profile": {k: me.get(k) for k in
                    ("username", "trust", "num_solved_prob", "num_submitted_prob")},
        "theorems": theorems,
        "submissions": submissions,
        "watchlist": sorted(watch),
    }


def diff(old, new):
    lines = []

    po, pn = old.get("profile", {}), new["profile"]
    for field, label in (("trust", "trust score"),
                         ("num_solved_prob", "problems solved"),
                         ("num_submitted_prob", "problems submitted")):
        a, b = po.get(field), pn.get(field)
        if a is not None and a != b:
            lines.append(f"- {label}: {a} -> {b}")

    to, tn = old.get("theorems", {}), new["theorems"]
    for tid, t in tn.items():
        if tid not in to:
            lines.append(f"- new theorem published: {t['name']} ({t['status']})")
            lines.append(f"    {t['title']}")
            lines.append(f"    {SITE}/theorems/{tid}")
        else:
            if to[tid]["status"] != t["status"]:
                lines.append(
                    f"- STATUS CHANGE: {t['name']} {to[tid]['status']} -> {t['status']}")
                lines.append(f"    {SITE}/theorems/{tid}")
            if to[tid].get("votes", 0) != t["votes"]:
                lines.append(
                    f"- votes on {t['name']}: {to[tid].get('votes', 0)} -> {t['votes']}")

    # ERROR is a server-side infrastructure fault, not news; the retry shows up anyway.
    so = old.get("submissions", {})
    sn = {k: v for k, v in new["submissions"].items() if v.get("status") != "ERROR"}
    for sid, s in sn.items():
        if sid not in so:
            lines.append(f"- new submission on {s['theorem_name']}: {s['status']}")
            lines.append(f"    {SITE}/submissions/{sid}")
            lines.append(f"    {SITE}/theorems/{s['theorem_id']}")
        elif so[sid].get("status") != s.get("status"):
            lines.append(f"- submission verdict on {s['theorem_name']}: "
                         f"{so[sid].get('status')} -> {s['status']}")
            lines.append(f"    {SITE}/submissions/{sid}")

    return lines


def main():
    write = "--write" in sys.argv
    try:
        token = access_token(read_key())
        uid, new = snapshot(token, load_state())
    except urllib.error.URLError as exc:
        sys.exit(f"prove2me unreachable: {exc}")

    old = load_state()
    lines = diff(old, new)
    first_run = not old.get("theorems")

    if first_run:
        print(f"prove2me: first run, recording baseline for {new['profile']['username']}")
        print(f"  profile: {SITE}/users/{uid}")
        print(f"  watching {len(new['theorems'])} theorem(s)")
    elif lines:
        print("prove2me: changes since last run")
        print("\n".join(lines))
    else:
        print("prove2me: no changes")

    if write:
        os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
        with open(STATE_PATH, "w") as fh:
            json.dump(new, fh, indent=1, sort_keys=True)
            fh.write("\n")
        print(f"\nstate written to {os.path.relpath(STATE_PATH, ROOT)}")


if __name__ == "__main__":
    main()
