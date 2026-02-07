"""https://leetcode.com/problems/intersection-of-two-arrays/description/"""


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))


s = Solution()

# Example 1
result = s.intersection([1, 2, 2, 1], [2, 2])
assert sorted(result) == [2]

# Example 2
result = s.intersection([4, 9, 5], [9, 4, 9, 8, 4])
assert sorted(result) == [4, 9]

print("All test cases passed!")
