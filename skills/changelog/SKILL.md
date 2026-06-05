---
name: changelog
description: Turn a list of commits or changes into a release changelog (Keep a Changelog format). Use when preparing release notes.
license: MIT
---

# Changelog

Turn the user's raw list of commits/changes into clean release notes in the
[Keep a Changelog](https://keepachangelog.com) style.

Format:
```
## [<version>] - <YYYY-MM-DD>

### Added
- …
### Changed
- …
### Fixed
- …
### Removed
- …
### Deprecated
- …
### Security
- …
```

Rules:
- Group each change under the right heading; **omit headings with no entries**.
- Rewrite commit shorthand into clear, user-facing language ("Fixed crash when opening empty files", not "fix npe in FileView").
- One bullet per meaningful change; merge duplicates; drop noise (merge commits, formatting-only churn) unless notable.
- Use the version/date if the user gives them; otherwise leave `[Unreleased]` and `<YYYY-MM-DD>` placeholders.
- Lead with what matters most to users. Output only the changelog.
