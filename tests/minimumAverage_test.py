from src.minimumAverage import Solution

s = Solution()


def test_example1():
    assert s.minimumAverage([7, 8, 3, 4, 15, 13, 4, 1]) == 5.5


def test_example2():
    assert s.minimumAverage([1, 9, 8, 3, 10, 5]) == 5.5


def test_example3():
    assert s.minimumAverage([1, 2, 3, 7, 8, 9]) == 5.0
