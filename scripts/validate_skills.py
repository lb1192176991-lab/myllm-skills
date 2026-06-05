#!/usr/bin/env python3
"""Validate the skills catalogue: every SKILL.md parses, names are well-formed,
and skills.json matches the files on disk. Run locally with:

    python3 scripts/validate_skills.py

Exits non-zero (and prints what's wrong) on any problem, so CI can gate PRs.
"""
import glob
import json
import os
import sys

ALLOWED = set("abcdefghijklmnopqrstuvwxyz0123456789-_")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def fail(msg):
    print(f"  ❌ {msg}")


def parse_frontmatter(path):
    """Return (fields, error). fields is a dict of frontmatter key->value."""
    with open(path, encoding="utf-8") as f:
        text = f.read().replace("\r\n", "\n")
    lines = text.split("\n")
    i = 0
    while i < len(lines) and lines[i].strip() == "":
        i += 1
    if i >= len(lines) or lines[i].strip() != "---":
        return None, "must start with a `---` frontmatter block"
    start = i + 1
    end = -1
    for j in range(start, len(lines)):
        if lines[j].strip() == "---":
            end = j
            break
    if end < 0:
        return None, "frontmatter `---` is never closed"
    fields = {}
    for line in lines[start:end]:
        t = line.strip()
        if not t or t.startswith("#") or ":" not in t:
            continue
        k, v = t.split(":", 1)
        fields[k.strip().lower()] = v.strip()
    return fields, None


def main():
    errors = 0
    manifest_path = os.path.join(ROOT, "skills.json")

    try:
        with open(manifest_path, encoding="utf-8") as f:
            manifest = json.load(f)
    except Exception as e:
        print(f"❌ skills.json is not valid JSON: {e}")
        return 1

    entries = manifest.get("skills", [])
    by_name = {}
    for e in entries:
        name = e.get("name", "")
        path = e.get("path", "")
        if not name or not path:
            fail(f"skills.json entry missing name or path: {e}")
            errors += 1
            continue
        if name in by_name:
            fail(f"duplicate skill name in skills.json: {name}")
            errors += 1
        by_name[name] = path
        if not os.path.exists(os.path.join(ROOT, path)):
            fail(f"skills.json lists {name} at {path}, but that file is missing")
            errors += 1

    files = sorted(glob.glob(os.path.join(ROOT, "skills", "*", "SKILL.md")))
    seen = set()
    for path in files:
        rel = os.path.relpath(path, ROOT)
        fields, err = parse_frontmatter(path)
        if err:
            fail(f"{rel}: {err}")
            errors += 1
            continue
        name = fields.get("name", "").lower()
        desc = fields.get("description", "")
        if not name:
            fail(f"{rel}: frontmatter missing `name`")
            errors += 1
            continue
        if not all(c in ALLOWED for c in name):
            fail(f"{rel}: invalid name '{name}' (use a-z, 0-9, hyphen, underscore)")
            errors += 1
        if not desc:
            fail(f"{rel}: frontmatter missing `description`")
            errors += 1
        if name in seen:
            fail(f"{rel}: duplicate skill name '{name}'")
            errors += 1
        seen.add(name)
        if name not in by_name:
            fail(f"{rel}: '{name}' is not listed in skills.json")
            errors += 1
        elif by_name[name] != rel:
            fail(f"{rel}: skills.json path for '{name}' is {by_name[name]}, expected {rel}")
            errors += 1

    for name, path in by_name.items():
        full = os.path.join(ROOT, path)
        if full not in files:
            fail(f"skills.json lists '{name}' at {path}, but it's not a skills/<name>/SKILL.md")
            errors += 1

    if errors:
        print(f"\n{errors} problem(s) found. See above.")
        return 1
    print(f"✅ {len(files)} skills valid and consistent with skills.json.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
