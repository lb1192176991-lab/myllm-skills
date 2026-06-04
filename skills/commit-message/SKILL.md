---
name: commit-message
description: Write a Conventional Commits message from a description of code changes. Use when the user asks for a commit message or describes a diff.
license: MIT
---

# Conventional Commit message

Produce a commit message in Conventional Commits format from the user's description of the change.

Format:
```
<type>(<optional scope>): <concise summary in imperative mood>

<optional body: what changed and why, wrapped at ~72 cols>
```

Allowed types: feat, fix, docs, style, refactor, perf, test, build, ci, chore.

Rules:
- Summary ≤ 72 chars, imperative ("add", not "added"), no trailing period.
- Pick the single most accurate type; use `!` after type/scope for a breaking change and add a `BREAKING CHANGE:` footer.
- Only describe what the user actually told you changed — don't invent scope.
- Output only the message, inside one code block.
