"""
O(n) - must check every number; digit counting via str() is O(d) per number,
but d is bounded by the constraint (nums[i] <= 10^5), making it constant.
"""

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for n in nums if len(str(n)) % 2 == 0)
