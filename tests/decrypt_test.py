from src.decrypt import Solution

s = Solution()


def test_example1():
    assert s.decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]


def test_example2():
    assert s.decrypt([1, 2, 3, 4], 0) == [0, 0, 0, 0]


def test_example3():
    assert s.decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13]


def test_example4():
    assert s.decrypt([5, 2, 2, 3, 1], 3) == [7, 6, 9, 8, 9]
