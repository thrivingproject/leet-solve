# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

LeetCode practice solutions in C, C++, and Python. Each file in `src/` is a standalone solution named after its function/approach, with the LeetCode problem number in a comment at the top.

## Claude's Role

Do not add, modify or suggest changes to the solution code unless explicitly asked. Do not attempt to build or execute the code—the user will do this. Only do one of the following based on the prompt:

### Action 1: write test cases

When writing tests, follow the existing pattern:

- Use `assert` statements in a `main()` function for C++
- For Python, create a pytest-style test file in `tests/` named `{moduleName}_test.py`:
  - Import with `from src.{moduleName} import Solution`
  - Create a module-level `s = Solution()` instance
  - Write plain `def test_*()` functions with `assert` statements (no unittest classes)
- For TypeScript use "node:assert" with // @ts-ignore
- Include test cases from the problem description on leetcode (don't try to fetch) no need to make up your own
- Put headers at top of file

### Action 2: Add documentation

Write the logic/strategy as a block comment. Make sure to include main problem tag (eg. sliding window, two pointers, etc). Also include the overall time complexity and reasoning.

- For python put the logic in a docstring as a module comment
- For C put the logic in a javadoc style comment
- Block comment should include overall time complexity and memory complexity
- Use the variable `n` when it makes sense, i.e. O(n), otherwise explain the variable
- Don't try to fetch anything
- Don't write the problem description
