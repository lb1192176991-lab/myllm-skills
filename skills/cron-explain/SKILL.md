---
name: cron-explain
description: Explain what a cron expression does in plain English, and optionally suggest corrections or alternatives.
license: MIT
---

# cron-explain — translate cron expressions to plain English

Given a cron expression (5- or 6-field standard), produce a human-readable description, flag edge cases, and suggest alternatives if common patterns would be clearer.

## Input

A cron expression like `*/15 * * * *` or a `crontab.guru` link.

## Output format

```
## Expression
`<cron expression>`

## In plain English
This runs <frequency description>.

For example:
<one or two concrete next-run times>

## ⚠️ Notes
- <any edge cases: DST overlaps, non-standard ranges, month/day-of-week intersection gotchas>
- <month (4th field) uses 1=Jan, day-of-week (5th field) uses 0=Sun>

## Suggested alternative
If <intent>, consider `<alternative expression>` which <reason>.
```

## Standard fields

```
┌───────── minute (0–59)
│ ┌──────── hour (0–23)
│ │ ┌─────── day of month (1–31)
│ │ │ ┌────── month (1–12)
│ │ │ │ ┌───── day of week (0–6, 0=Sun, 7=Sun)
* * * * *
```

## Edge cases to flag

1. **Day-of-week × day-of-month both non-\*** — these OR in most cron implementations (contradicts intuition)
2. **DST transitions** — `0 2 * * *` may run 2× or 0× on DST change days
3. **`0 0 1 1 *`** — runs every January 1st at midnight (minute=0, hour=0, day-of-month=1, month=1)
4. **`@yearly` or `@annually`** — alias for `0 0 1 1 *`
5. **Non-standard ranges** — warn if values exceed standard ranges (e.g., minute > 59)
6. **`H` notation** — if Jenkins-style `H` is detected, note this is a Jenkins hash, not standard cron

## Examples

| Expression | Meaning |
|---|---|
| `*/15 * * * *` | Every 15 minutes |
| `0 9 * * 1-5` | Weekdays at 9:00 AM |
| `0 0 1 */3 *` | First day of every quarter at midnight |
| `30 4 2 * *` | 4:30 AM on the 2nd of every month |
| `0 0 * * 0` | Every Sunday at midnight |
