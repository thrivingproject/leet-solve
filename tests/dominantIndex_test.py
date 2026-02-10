from src.dominantIndex import Solution

s = Solution()


def test_example1():
    assert s.dominantIndex([3, 6, 1, 0]) == 1


def test_example2():
    assert s.dominantIndex([1, 2, 3, 4]) == -1


def test_example3():
    assert s.dominantIndex([1, 0]) == 0
