"""
Sliding Window

Maintain a window [left, right] where the k-constraint holds (at least one
of the 0-count or 1-count is <= k). Track counts of 0s and 1s as the window
moves. Expand right each iteration; if both counts exceed k, shrink from
the left until validity is restored.

TODO: explain r - l + 1

Time Complexity: O(n) - each element is visited at most twice (once by each pointer)
Space Complexity: O(1) - only tracking two counters
"""


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        count = 0
        l = 0
        zeroes = ones = 0
        for r in range(len(s)):
            if s[r] == "0":
                zeroes += 1
            else:
                ones += 1
            while zeroes > k and ones > k:
                if s[l] == "0":
                    zeroes -= 1
                else:
                    ones -= 1
                l += 1
            count += r - l + 1
        return count
