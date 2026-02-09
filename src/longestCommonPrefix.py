"""
Find the longest common prefix among all strings by using the first string
as a reference and comparing each character position across all other strings.
If any string is shorter or has a different character at that position, we
truncate the prefix there.

Time: O(n * m) where n = number of strings, m = length of shortest string
Space: O(1) — only storing an index
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        for i, char in enumerate(strs[0]):  # O(m) iterate chars of first string
            for word in strs[1:]:  # O(n)
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]

        return strs[0]


# Tests
sol = Solution()
assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
print("All test cases passed!")
