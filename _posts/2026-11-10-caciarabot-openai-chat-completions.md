---
title: "caciarabot: one chat-completions client instead of a Gemini one, so the model provider is a base URL"
date: 2026-11-10
tags: [bot, telegram]
---

[caciarabot](https://github.com/carlok/caciarabot) no longer has a Gemini client: `app/caciarabot/llm/gemini.py` is gone and `llm/chat_completions.py` POSTs to `{CACIARABOT_LLM_BASE_URL}/chat/completions`, the one wire format Gemini, OpenAI, OpenRouter, Ollama and Anthropic's compatibility layer all accept. The default base URL is Gemini's own OpenAI-compatible endpoint, so nothing changes on Gemini, and moving elsewhere is a base URL, a key and a model name ([c98771f](https://github.com/carlok/caciarabot/commit/c98771f), merged as [59bcecc](https://github.com/carlok/caciarabot/commit/59bcecc)).

The key handling is the careful part, since a key travels with the request: `LLM_API_KEY` is the key, `GEMINI_API_KEY` is still read but only while the base URL is Gemini's, so a leftover Gemini key is never sent to another host, redirects are not followed for the same reason, and `runtime.gemini_api_key` became `llm_api_key`. The new setting is validated as an http(s) URL at config load, so a typo fails `caciarabot-validate` instead of at the first reply, and `tests/test_chat_completions.py` runs the client against a local `aiohttp` server rather than a provider.
