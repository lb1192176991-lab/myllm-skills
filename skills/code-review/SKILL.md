---
name: code-review
description: Review a code snippet for bugs, security issues, and style, with concrete fixes. Use when the user shares code and asks for feedback or a review.
license: MIT
---

# Code review

Review the provided code. Structure the response as:

## Bugs & correctness
- Each issue with a one-line explanation and a suggested fix.

## Security
- Injection, secrets in source, unsafe input handling, etc. (or "none found").

## Style & clarity
- Naming, structure, dead code — only changes that actually matter.

## Suggested patch
- A short corrected snippet for the most important fix.

Rules:
- Be specific and cite the line or symbol you mean.
- Don't rewrite the whole thing unless asked.
- If the code is fine, say so plainly rather than inventing problems.
- Match the language's idioms; don't impose another language's conventions.
