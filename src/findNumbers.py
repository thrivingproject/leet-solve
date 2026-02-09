"""
O(n) - must check every number; digit counting via str() is O(d) per number,
but d is bounded by the constraint (nums[i] <= 10^5), making it constant.
"""

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for n in nums if len(str(n)) % 2 == 0)


s = Solution()
assert s.findNumbers([12, 345, 2, 6, 7896]) == 2
assert s.findNumbers([555, 901, 482, 1771]) == 1
print("All test cases passed!")
