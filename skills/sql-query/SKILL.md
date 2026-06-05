---
name: sql-query
description: Write a SQL query from a plain-English request and a table schema. Use when the user wants a query written, explained, or fixed.
license: MIT
---

# SQL query

Translate the user's request into a correct SQL query.

1. Work from the schema the user provides. If the relevant tables/columns aren't given, ask for them (or state the assumptions you're making).
2. Output:

   ```sql
   -- one clear query
   ```

   Then **two lines** explaining what it does and any assumption (e.g. dialect).

Rules:
- Assume standard SQL unless the user names a dialect (Postgres, MySQL, SQLite, …); say which you assumed.
- Use explicit column lists and `JOIN ... ON`, not implicit joins. Alias tables for readability.
- For user-supplied values, use parameter placeholders (`?` / `:name`) and note it — never concatenate raw input.
- Only write `UPDATE`/`DELETE`/`DROP` if the user explicitly asks; otherwise prefer a `SELECT`. For destructive statements, add a one-line warning and suggest a `SELECT` to preview affected rows first.
- If asked to fix a query, show the corrected version and name the bug.
