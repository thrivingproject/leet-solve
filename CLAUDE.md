# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

LeetCode practice solutions in C, C++, and Python. Each file in `src/` is a standalone solution named after its function/approach, with the LeetCode problem number in a comment at the top.

## Claude's Role

**Primary purpose: Write test cases.** Do not modify or suggest changes to the solution code unless explicitly asked. Do not attempt to build or execute the code—the user will do this.

When writing tests, follow the existing pattern:

- Use `assert` statements in a `main()` function for C++
- For Python just write script code beneath the Solution class (no function needed)
- For TypeScript use "node:assert" with // @ts-ignore
- Include test cases from the problem description on leetcode (don't try to fetch) no need to make up your own
- Print "All test cases passed!" on success
- Put headers at top of file
