from math import inf


class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        n = len(nums)
        nums.sort()
        smallest = inf
        l, r = 0, n - 1
        for i in range(n // 2):
            smallest = min(smallest, (nums[l] + nums[r]) / 2)
            l += 1
            r -= 1
        return smallest
