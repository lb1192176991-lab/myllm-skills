---
name: email-reply
description: Draft a clear, professional email reply from a few bullet points and the desired tone. Use when the user wants help responding to an email.
license: MIT
---

# Draft an email reply

From the user's bullet points (and the original email if provided), write a reply.

- Open with an appropriate greeting; close with a sign-off.
- Cover every bullet; don't add commitments the user didn't make.
- Match the requested tone (default: warm but professional). Keep it tight — no filler.
- If key info is missing (a date, a name, a figure), leave a clearly marked `[placeholder]` rather than inventing it.
- Mirror the original email's level of formality when one is supplied.

Output just the email — an optional subject line, then the body. No commentary before or after.
