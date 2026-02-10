"""
1004. Max Consecutive Ones III

Use a sliding window [left, right] tracking the number of zeros flipped.
Expand right; when zeros exceed k, shrink left until zeros <= k.
Track the max window size throughout.

Time: O(n)  Space: O(1)
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left_index = 0
        zeros = 0
        max_ones = 0

        for right_index in range(len(nums)):  # O(n)
            if nums[right_index] == 0:
                zeros += 1
            while zeros > k:
                if nums[left_index] == 0:
                    zeros -= 1
                left_index += 1
            max_ones = max(max_ones, right_index - left_index + 1)

        return max_ones
