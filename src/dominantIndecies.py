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


s = Solution()
assert s.dominantIndices([5, 4, 3]) == 2
assert s.dominantIndices([4, 1, 2]) == 1
print("All test cases passed!")
