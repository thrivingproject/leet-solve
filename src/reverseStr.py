"""
# 541. Reverse String II

Strategy: Two Pointers / String Manipulation
Iterate through the string in chunks of 2k characters. For each chunk,
reverse the first k characters and leave the rest as-is. Slicing handles
the edge case where fewer than k characters remain — reversing a shorter
slice naturally produces the correct result.

Time Complexity: O(n) — each character is visited once across all chunks.
Space Complexity: O(n) — a new string is built since strings are immutable.
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        new_s = ""
        i = 0
        while i < len(s):
            sub_str = s[i : i + 2 * k]
            new_s += sub_str[k - 1 :: -1] + sub_str[k:]
            i += 2 * k
        return new_s
