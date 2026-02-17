class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even = 0
        odd = 1
        while odd < len(nums):
            while even < len(nums) and nums[even] % 2 == 0:
                even += 2
            while odd < len(nums) and nums[odd] % 2 == 1:
                odd += 2
            if odd < len(nums) and even < len(nums):
                nums[odd], nums[even] = nums[even], nums[odd]
        return nums
