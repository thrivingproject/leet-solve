class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            right_sum = total - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1


s = Solution()
assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
assert s.pivotIndex([1, 2, 3]) == -1
assert s.pivotIndex([2, 1, -1]) == 0
print("All test cases passed!")
