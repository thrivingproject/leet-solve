from src.pivotIndex import Solution

s = Solution()


def test_example1():
    assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3


def test_example2():
    assert s.pivotIndex([1, 2, 3]) == -1


def test_example3():
    assert s.pivotIndex([2, 1, -1]) == 0
