"""
# 2460. Apply Operations to an Array

## Two Pointers

Two-pass approach:
1. First pass applies the doubling operation: iterate through the array and
   whenever two adjacent elements are equal, double the first and zero the second.
2. Second pass moves all zeros to the end using a write pointer. Iterate through
   the array and swap each non-zero element to the write position, then advance
   the write pointer. This partitions non-zeros to the front in their original
   order.

Time complexity: O(n) — two sequential linear passes over the array.
Space complexity: O(1) — all operations are done in-place.
"""


class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        write = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write], nums[i] = nums[i], nums[write]
                write += 1

        return nums
