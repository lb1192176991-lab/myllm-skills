---
name: summarize-url
description: Summarize a web page or article from a URL. Use when the user shares a link and wants the gist or key points.
license: MIT
---

# Summarize a URL

When the user gives a link (or asks you to summarise one), fetch it and summarise.

1. Use the `fetch_url` tool to retrieve the page. If it fails or the page is paywalled/empty, use `web_search` for the title to find a readable source — and say if you couldn't read the original.
2. Produce:

   **TL;DR** — 1–2 sentences.

   **Key points**
   - 3–6 bullets capturing the substance.

   **Worth knowing** (optional) — caveats, bias, date, or who published it.

Rules:
- Summarise only what the page actually says — never fill gaps from memory.
- Keep names, numbers, and quotes accurate.
- If the content is time-sensitive, note its date.
- Don't paste the whole article back; distil it.
