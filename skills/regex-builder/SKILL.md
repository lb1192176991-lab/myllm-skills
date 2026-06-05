---
name: regex-builder
description: Build and explain a regular expression from a description, with examples. Use when the user needs a regex or wants one explained.
license: MIT
---

# Regex builder

Produce a regular expression that matches what the user described.

Output:

1. The pattern in a code block:
   ```
   <regex>
   ```
2. **How it works** — break the pattern into parts and explain each in one line.
3. **Matches** — 2–3 example strings it accepts.
4. **Doesn't match** — 2–3 it rejects.

Rules:
- State the flavour (JavaScript, PCRE, Python `re`, …); default to JavaScript and say so. Note any flags (e.g. `i`, `g`, `m`).
- Keep it as simple as possible — readable beats clever. Anchor with `^`/`$` when the whole string must match.
- Escape special characters correctly and call out catastrophic-backtracking risks if the pattern is complex.
- If the user pastes a regex to explain, skip straight to **How it works** + examples.
