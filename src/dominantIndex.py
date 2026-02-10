"""
Find the index of the largest element if it is at least twice as large
as every other element.

Track the max and second max in a single pass. If max >= 2 * second_max,
return the index of max; otherwise return -1.
"""

from math import inf


class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        ans = 0
        first = nums[0]
        second = -inf

        for i in range(1, len(nums)):  # O(n) single pass
            if nums[i] > first:
                second = first
                first = nums[i]
                ans = i
            elif nums[i] > second:
                second = nums[i]

        return ans if first >= 2 * second else -1  # O(1) comparison
