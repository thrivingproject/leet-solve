"""
Sliding Window

Use two pointers to maintain a window where the k-constraint is satisfied.
Track counts of 0s and 1s in the current window.

For each right endpoint, expand the window by including s[right] and
updating its count. If the window becomes invalid (both counts > k),
shrink from the left until validity is restored. Then count all valid
substrings ending at right.

Once the window [left, right] is valid, every substring that ends at right
and starts at any index i where left <= i <= right is also valid. This is
because shrinking a valid window from the left can only decrease (or keep
equal) the counts of 0s and 1s, so the constraint remains satisfied.

Every substring has exactly one right endpoint. At each iteration we only
count substrings whose right endpoint is the current right — there are
(right - left + 1) of them, one per valid starting index in [left, right].
Since right advances by 1 each iteration, no substring is ever counted
twice: a substring counted at right=2 ends at index 2, and a substring
counted at right=3 ends at index 3 — they are different substrings.

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
