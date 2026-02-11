# 3285. Find Indices of Stable Mountains
from src.stableMountains import Solution

s = Solution()


def test_example1():
    assert s.stableMountains([1, 2, 3, 4, 5], 2) == [3, 4]


def test_example2():
    assert s.stableMountains([10, 1, 10, 1, 10], 3) == [1, 3]


def test_example3():
    assert s.stableMountains([10, 1, 10, 1, 10], 10) == []
