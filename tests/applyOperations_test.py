# 2460. Apply Operations to an Array

from src.applyOperations import Solution

s = Solution()


def test_example1():
    assert s.applyOperations([1, 2, 2, 1, 1, 0]) == [1, 4, 2, 0, 0, 0]


def test_example2():
    assert s.applyOperations([0, 1]) == [1, 0]


def test_example3():
    assert s.applyOperations(
        [847, 847, 0, 0, 0, 399, 416, 416, 879, 879, 206, 206, 206, 272]
    ) == [1694, 399, 832, 1758, 412, 206, 272, 0, 0, 0, 0, 0, 0, 0]
