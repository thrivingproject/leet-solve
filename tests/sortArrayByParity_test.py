# 905. Sort Array By Parity
from src.sortArrayByParity import Solution

s = Solution()


def test_example1():
    result = s.sortArrayByParity([3, 1, 2, 4])
    assert all(x % 2 == 0 for x in result[:2])
    assert all(x % 2 == 1 for x in result[2:])


def test_example2():
    result = s.sortArrayByParity([0])
    assert result == [0]


def test_example3():
    result = s.sortArrayByParity([0, 2])
    assert result == [0, 2]


def test_example4():
    assert s.sortArrayByParity([0, 2, 1]) == [0, 2, 1]
