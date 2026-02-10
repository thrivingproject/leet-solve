# TODO: optimize
class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        n = len(nums)
        max_or = 0
        for num in nums:
            max_or |= num
        count = 0
        for i in range(1, 2**n):
            bit_or = 0
            for j in range(n):
                if (i >> j) & 1:
                    bit_or |= nums[j]
            if bit_or == max_or:
                count += 1
        return count
