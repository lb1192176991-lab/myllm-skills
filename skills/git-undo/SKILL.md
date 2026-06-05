---
name: git-undo
description: Given a described git mistake (bad commit, wrong branch, accidental add), suggest the safest command(s) to fix it, explain what each does, and warn before anything destructive.
license: MIT
---

# git-undo — safely fix common git mistakes

Given a *description* of the mistake (not raw git commands), this skill prints the safest sequence of commands to undo it, explains what each command does, and marks destructive commands with ⚠️.

## Common scenarios

### 1. I committed to the wrong branch

```
# Current state: commit on `main` that should be on `feature/foo`
git checkout feature/foo
git cherry-pick main           # copy the commit over
git checkout main
git reset --hard HEAD~1        # ⚠️ DESTRUCTIVE — removes commit from main
git push --force-with-lease    # ⚠️ only if main was already pushed
```

**Explain:** cherry-pick copies the commit, `reset --hard` on main rewinds it, `--force-with-lease` safely overwrites the remote (won't clobber others' work).

### 2. I accidentally added a file (git add) that I didn't want

```
git reset HEAD <file>
```

or to unstage everything

```
git reset
```

**Explain:** `git reset` without a commit reference moves the staging area (index) back to the last commit. No data is lost — the file stays modified in the working tree.

### 3. I want to undo my last commit but keep the changes

```
git reset --soft HEAD~1
```

**Explain:** Moves HEAD back by one commit but keeps the changes staged (`--soft`). Safer than `--hard` which discards changes.

### 4. I want to edit the last commit's message

```
git commit --amend -m "New message"
```

**Explain:** Rewrites the most recent commit with a new message. Only for commits that haven't been pushed yet — amending a pushed commit rewrites history.

### 5. I committed and realized there's a typo / forgot a file

```
git add <fixed-file>
git commit --amend --no-edit
```

**Explain:** Stages the fix first, then amends the previous commit without changing its message.

## Safety rules

- **Never** suggest `git push --force` without `--force-with-lease` or `--force-if-includes`.
- **Never** suggest `git reset --hard` on a branch that others might depend on without first checking if it's pushed.
- **Never** suggest `git rebase` on a public/shared branch.
- If the user mentions they already pushed the broken commit, always prefer revert over reset+force-push.
- When suggesting `rm -rf .git` or anything involving `--hard`, preface with a ⚠️ and suggest backing up first.

## Output format

```
## Problem: <one-line restatement of the mistake>

## Safe fix (recommended)
<command sequence>

## What this does
<explanation>

## ⚠️ Caveats
<any destructive or irreversible consequences>
```
