---
name: research-brief
description: Answer a question with a short, sourced research brief. Use for "research X", "what's the latest on Y", or fact-finding that needs citations.
license: MIT
---

# Research brief

Answer the user's question with a concise, sourced brief — not a wall of text.

1. Run `web_search` with 2–4 focused queries (vary the angle; don't repeat one phrasing). Open the most promising results with `fetch_url` when you need detail.
2. Synthesise across sources. Structure the answer as:

   **Answer** — the direct conclusion in 2–4 sentences.

   **What the sources say**
   - Bullet each substantive finding, each followed by its source link.

   **Confidence & gaps** — how solid this is, and what's still uncertain or contested.

   **Sources**
   - Title — URL (one per source actually used).

Rules:
- Cite only links that came back from a tool. Never invent or guess a URL.
- Prefer primary/recent sources; flag when sources disagree.
- Date-stamp time-sensitive claims; today's date is authoritative.
- If the tools return nothing usable, say so plainly rather than guessing.
