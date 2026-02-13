"""
# 977. Squares of a Sorted Array

## Two Pointers (outside-in)

The input is sorted, so the largest squared values are at the extremes
(most negative on the left, most positive on the right). Two pointers
start at opposite ends and we fill the result array from back to front,
always placing the larger absolute value's square next.

## Complexity
- Time: O(n) — single pass through the array
- Space: O(n) — output array
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        size = len(nums)
        squares = [0] * size
        l, r = 0, size - 1
        for i in range(size - 1, -1, -1):
            if nums[r] > abs(nums[l]):
                squares[i] = nums[r] ** 2
                r -= 1
            else:
                squares[i] = nums[l] ** 2
                l += 1
        return squares
