class Solution:
    def minOperations(self, nums: list[int]) -> int:
        flips = 0
        for i in range(len(nums) - 2):
            if not nums[i]:
                nums[i] = int(not nums[i])
                nums[i + 1] = int(not nums[i + 1])
                nums[i + 2] = int(not nums[i + 2])
                flips += 1
        if sum(nums) == len(nums):
            return flips
        return -1


s = Solution()
assert s.minOperations([0, 1, 1, 1, 0, 0]) == 3
assert s.minOperations([0, 1, 1, 1]) == -1
