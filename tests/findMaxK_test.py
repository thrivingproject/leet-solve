# 2441. Largest Positive Integer That Exists With Its Negative
from src.findMaxK import Solution

s = Solution()


def test_example1():
    assert s.findMaxK([-1, 2, -3, 3]) == 3


def test_example2():
    assert s.findMaxK([-1, 10, 6, 7, -7, 1]) == 7


def test_example3():
    assert s.findMaxK([-10, 8, 6, 7, -2, -3]) == -1
