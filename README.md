# MyLLM Skills

A curated, open collection of **Skills** for [MyLLM](https://apps.apple.com/gb/app/myllm-local-ai-agent/id6760704297) — the private, on-device AI agent for iOS.

A **Skill** is a small bundle of reusable instructions in the open **Agent-Skill format**: a `SKILL.md` file with simple frontmatter (`name`, `description`) followed by a markdown body of guidance. MyLLM shows the model each skill's name and description, and loads the full instructions **on demand** when a task matches — so skills add know-how without bloating every prompt.

These skills are **instruction-only** (Tier 1): they contain no scripts and no network calls. The model follows them using the tools it already has.

## Install

**From the app (recommended)** — in any chat:

```
/skill add teamdzx/myllm-skills
/skill install meeting-notes@teamdzx
```

…or install everything by name, e.g. `/skill install code-review@teamdzx`.

**Direct, one tap** — open a skill's `SKILL.md` URL or use a deep link:

```
/skill install https://raw.githubusercontent.com/TeamDzX/myllm-skills/main/skills/meeting-notes/SKILL.md
```

**From the Marketplace** — browse and tap **Install skill** at
[opticell-limited.com/myllm-wiki#skills](https://www.opticell-limited.com/myllm-wiki#skills).

Every install asks you to confirm in the app first.

## What's inside

| Skill | What it does |
|-------|--------------|
| `meeting-notes` | Turn raw notes or a transcript into clean minutes |
| `commit-message` | Write a Conventional Commits message from a change description |
| `email-reply` | Draft a professional email reply from bullet points |
| `code-review` | Review a snippet for bugs, security, and style |
| `flashcards` | Turn notes or a topic into Q/A study flashcards |
| `explain-simply` | Explain a complex topic in plain language with an analogy |

## Layout

```
skills/
  <skill-name>/
    SKILL.md       # frontmatter (name, description) + instructions
skills.json        # machine-readable index of the above
```

## The SKILL.md format

```markdown
---
name: my-skill
description: One line — what it does and when to use it. This drives discovery, so write it like a trigger.
license: MIT
---

# My skill

Step-by-step instructions the model should follow when this skill is loaded.
Keep it focused. Reference the model's normal tools where useful.
```

Name must be lowercase letters, digits, hyphen, or underscore. Description must be a single line.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). PRs welcome — one skill per folder, instruction-only.

## License

[MIT](LICENSE) — use, modify, and redistribute freely, with attribution.
