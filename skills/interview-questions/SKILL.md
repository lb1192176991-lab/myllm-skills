---
name: interview-questions
description: Generate role-specific interview questions from a job title or description, grouped by theme (technical / behavioural / culture), with what a strong answer looks like.
license: MIT
---

# interview-questions — generate role-specific interview questions

Given a job title, job description, or both, generate a structured set of interview questions grouped by theme. Each question includes what a strong answer demonstrates.

## Input

A job title (e.g., "Senior Frontend Engineer") or a full job description URL/text.

## Output format

```
# Interview Questions for <Role>

## Technical
Based on the skills and tools mentioned in the description.

1. **<question>**
   *What a strong answer shows:* <2-3 sentence description>
   *Key points to cover:* <bullet points>

2. **<question>**
   ...
```

### Question categories (in order)

1. **Technical** — role-specific hard skills (coding, architecture, domain knowledge)
2. **Behavioural** — STAR-format questions about past work, conflict, ownership
3. **Culture & Collaboration** — team dynamics, async work, code review philosophy
4. **Problem-Solving** — open-ended scenario or design questions
5. **Role-Specific** — if mentioned in the description: (e.g. "this role manages 3 ICs" → management questions)

### How many questions

- Technical: 4–6 depending on seniority
- Behavioural: 3–4
- Culture: 2–3
- Problem-Solving: 1–2
- Role-Specific: 2–3 if applicable

## Rules

1. **Extract specifics** from the job description: mention exact tools, languages, frameworks, and team size mentioned in the JD.
2. **No generic questions** like "Where do you see yourself in 5 years?" unless explicitly relevant.
3. **Match seniority**: Junior → focus on learning and fundamentals; Senior → focus on ownership, architecture, mentoring; Staff+ → focus on org-wide impact, strategy, ambiguity.
4. **Start with a summary line**: "<N> questions across <M> categories, tailored to <role> at <company>."
5. **End with a red-flag detection section** — note any concerns based on the JD text (e.g., "job description mentions 'rockstar' and 'wear many hats' — may indicate understaffing").

## Examples

### Input
"Senior Frontend Engineer at a Series B SaaS startup, React/TypeScript, 5+ years exp"

### Output summary
"15 questions across 5 categories, tailored to Senior Frontend Engineer at a Series B SaaS startup."

### Sample question
**Technical — React**

1. **How would you architect the state management for a real-time collaborative document editor?**
   *What a strong answer shows:* Understanding of CRDTs or OT, awareness of React's concurrency model, experience with WebSockets or SSE, and tradeoff analysis between different state management approaches.
   *Key points:* Mentions pros/cons of Zustand vs Jotai vs Redux for this use case; discusses optimistic updates and conflict resolution; acknowledges that "it depends" on team size and feature complexity.
