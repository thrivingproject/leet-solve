"""https://leetcode.com/problems/intersection-of-two-arrays/description/"""


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1) & set(nums2))
