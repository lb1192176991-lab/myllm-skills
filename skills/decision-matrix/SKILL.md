---
name: decision-matrix
description: Weigh options against weighted criteria to support a decision. Use when the user is choosing between alternatives.
license: MIT
---

# Decision matrix

Help the user choose between options by scoring them against weighted criteria.

1. Identify the **options** and the **criteria** that matter. If the user didn't give criteria, propose a sensible set and weights, and say you're assuming them.
2. Build a markdown table: one row per option, one column per criterion, scored **1–5**. Include each criterion's weight in its header.
3. Compute a **weighted total** per option (Σ score × weight) and add a Total column.
4. End with:

   **Recommendation** — the leading option in one sentence.

   **Main trade-off** — what you'd give up by choosing it.

Rules:
- Be explicit about assumptions and weights; the user can re-weight and you recompute.
- Score honestly — don't rig the matrix toward a predetermined answer.
- If two options are close, say so rather than forcing a winner.
- Keep it decision-useful, not exhaustive.
