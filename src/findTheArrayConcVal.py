class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1
        s = 0
        while l < r:
            s += int(str(nums[l]) + str(nums[r]))
            l += 1
            r -= 1
        if l == r:
            s += nums[l]
        return s
