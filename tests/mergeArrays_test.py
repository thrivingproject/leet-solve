# 2570. Merge Two 2D Arrays by Summing Values
from src.mergeArrays import Solution

s = Solution()


def test_example1():
    nums1 = [[1, 2], [2, 3], [4, 5]]
    nums2 = [[1, 4], [3, 2], [4, 1]]
    assert s.mergeArrays(nums1, nums2) == [[1, 6], [2, 3], [3, 2], [4, 6]]


def test_example2():
    nums1 = [[2, 4], [3, 6], [5, 5]]
    nums2 = [[1, 3], [4, 3]]
    assert s.mergeArrays(nums1, nums2) == [[1, 3], [2, 4], [3, 6], [4, 3], [5, 5]]
