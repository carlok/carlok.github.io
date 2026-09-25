---
title: "caciarabot: the secret feature logs how many people, not which ones"
date: 2026-09-25
tags: [bot, telegram]
---

The `segreto` feature in [caciarabot](https://github.com/carlok/caciarabot) keeps
a roster of who has posted — display names only, no message content, because the
Bot API cannot list a group's membership — but its dry-run log line wrote those
names out in full. It now logs a count instead
([db905db](https://github.com/carlok/caciarabot/commit/db905db)), and the
README's Privacy section says so explicitly: the events say how many people a
secret was about, never which ones. The change also cleared CodeQL alert
`py/clear-text-logging-sensitive-data`, whose "sensitive data" label was firing
on the word "secret" rather than on a credential — the dataflow was real even
where the rule's name was not, and the count is all the operator needs to see the
feature working.
