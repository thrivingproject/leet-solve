"""
# 821. Shortest Distance to a Character
# Two Pointers
#
# Pre-compute the indices where c occurs, then sweep through s maintaining
# two pointers (l, r) into that list — the nearest occurrence of c behind
# and ahead of the current position. For each index i, the answer is the
# min distance to indices[l] and indices[r]. Advance l and r as i passes
# each occurrence, clamping to stay in bounds.
#
# Time complexity: O(n) — one pass to collect indices, one pass to compute distances.
# Space complexity: O(n) — for the indices list and the answer array.
"""


class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        answer = []
        indices = [i for i in range(len(s)) if s[i] == c]
        l = r = 0
        for i in range(len(s)):
            answer.append(min(abs(indices[l] - i), abs(indices[r] - i)))
            if i >= indices[r]:
                r = min(r + 1, len(indices) - 1)
            if l + 1 < len(indices) and i >= indices[l + 1]:
                l = min(l + 1, max(len(indices) - 2, 0))

        return answer
