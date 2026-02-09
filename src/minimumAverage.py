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


# 3194. Minimum Average of Smallest and Largest Elements
s = Solution()
assert s.minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]) == 5.5
assert s.minimumAverage([1, 9, 8, 3, 10, 5]) == 5.5
assert s.minimumAverage([1, 2, 3, 7, 8, 9]) == 5.0
print("All test cases passed!")
