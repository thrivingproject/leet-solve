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


# 1679. Max Number of K-Sum Pairs
s = Solution()
assert s.maxOperations([1, 2, 3, 4], 5) == 2
assert s.maxOperations([3, 1, 3, 4, 3], 6) == 1
print("All test cases passed!")
