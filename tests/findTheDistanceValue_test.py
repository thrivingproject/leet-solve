# 1385. Find the Distance Value Between Two Arrays
from src.findTheDistanceValue import Solution

s = Solution()


def test_example1():
    assert s.findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2) == 2


def test_example2():
    assert s.findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3) == 2


def test_example3():
    assert s.findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6) == 1


def test_example4():
    assert s.findTheDistanceValue([4, -3, -7, 0, -10], [10], 69) == 0
