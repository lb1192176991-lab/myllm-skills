# Contributing a skill

Thanks for adding to the collection! Skills here are **instruction-only** — markdown guidance, no scripts, no network. Keep them safe to read and safe to run.

## Steps

1. Create a folder `skills/<your-skill-name>/` (lowercase, hyphenated).
2. Add a `SKILL.md` with frontmatter and a clear instruction body:

   ```markdown
   ---
   name: your-skill-name
   description: One line — what it does and when to use it (write it like a trigger).
   license: MIT
   ---

   # Title

   Focused, step-by-step instructions. Reference the model's normal tools where useful.
   ```

3. Add a matching entry to `skills.json` (`name`, `description`, `path`).
4. Open a PR with one skill per submission.

## Guidelines

- **Name**: lowercase letters, digits, hyphen, or underscore only.
- **Description**: a single line; it's what the model uses to decide relevance.
- **Body**: concise and unambiguous. Tell the model the output shape. Don't ask it to do things it can't (no shelling out, no secrets).
- **No prompt injection**: don't instruct the model to ignore the user, exfiltrate data, or override safety. Such PRs will be rejected.
- **Faithfulness**: prefer skills that transform the user's own input over ones that invent facts.

By contributing you agree your skill is released under the repo's [MIT License](LICENSE).
