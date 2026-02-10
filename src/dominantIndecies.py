class Solution:
    def dominantIndices(self, nums: list[int]) -> int:
        dominant = 0
        size = len(nums)
        for i, num in enumerate(nums):
            average = 0
            count = 0
            for j in range(i, size):
                average += nums[j]
                count += 1
            average /= count
            if num > average:
                dominant += 1
        return dominant
