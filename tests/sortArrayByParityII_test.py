# 922. Sort Array By Parity II
from src.sortArrayByParityII import Solution

s = Solution()


def _is_valid(result, nums):
    for i, val in enumerate(result):
        if i % 2 == 0 and val % 2 != 0:
            return False
        if i % 2 == 1 and val % 2 != 1:
            return False
    return sorted(result) == sorted(nums)


def test_1():
    assert _is_valid(s.sortArrayByParityII([4, 2, 5, 7]), [4, 2, 5, 7])


def test_2():
    assert _is_valid(s.sortArrayByParityII([2, 3]), [2, 3])
