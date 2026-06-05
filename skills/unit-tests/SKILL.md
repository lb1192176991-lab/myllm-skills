---
name: unit-tests
description: Write unit tests for a function or module. Use when the user shares code and wants tests for it.
license: MIT
---

# Unit tests

Write focused unit tests for the code the user provides.

1. Identify the language and test framework. If it's not obvious, pick the idiomatic default (e.g. pytest for Python, Jest for JS/TS, XCTest for Swift, JUnit for Java) and say which you used.
2. Cover, at minimum:
   - the happy path,
   - edge cases (empty/zero/boundary/large inputs),
   - error/invalid-input behaviour.
3. Output the tests in one runnable code block.

Rules:
- Use Arrange–Act–Assert and descriptive test names that state the expectation.
- Test observable behaviour and the public interface — not private implementation details.
- One logical assertion focus per test; avoid coupling tests to each other.
- Don't hit the network, clock, or filesystem — stub/mock those and note it.
- If a likely bug surfaces while writing tests, add a failing test for it and flag it briefly.
