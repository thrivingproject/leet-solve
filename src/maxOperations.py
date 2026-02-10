class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        n = 0
        while l < r:
            lr_sum = nums[l] + nums[r]
            if lr_sum < k:
                l += 1
            elif lr_sum > k:
                r -= 1
            else:
                n += 1
                l += 1
                r -= 1
        return n
