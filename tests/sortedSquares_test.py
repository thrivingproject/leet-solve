# 977. Squares of a Sorted Array
from src.sortedSquares import Solution

s = Solution()


def test_example1():
    assert s.sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]


def test_example2():
    assert s.sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]


def test_example3():
    assert s.sortedSquares([-1]) == [1]


def test_example4():
    assert s.sortedSquares([1]) == [1]
