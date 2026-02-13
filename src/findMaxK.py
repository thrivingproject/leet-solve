"""
This is listed as a two pointer problem, but that requires sorting
and leads to O(n*log n) time complexity. Faster to use a set and check
for each positive number if its negative is in the set.
"""


class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        nums_set = set(nums)
        largest = -1
        for num in nums:
            if num > 0 and -num in nums_set:
                largest = max(largest, num)
        return largest

    def findMaxK_two_pointer(self, nums: list[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r:
            if -nums[l] == nums[r]:
                return nums[r]
            elif abs(nums[l]) > nums[r]:
                l += 1
            else:
                r -= 1
        return -1
