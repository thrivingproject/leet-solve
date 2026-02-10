from src.mergeAdjacent import Solution

s = Solution()


def test_example1():
    assert s.mergeAdjacent([3, 1, 1, 2]) == [3, 4]


def test_example2():
    assert s.mergeAdjacent([2, 2, 4]) == [8]


def test_example3():
    assert s.mergeAdjacent([3, 7, 5]) == [3, 7, 5]


def test_example4():
    assert s.mergeAdjacent([2, 1, 1, 2]) == [4, 2]


def test_example5():
    assert s.mergeAdjacent([4, 2, 1, 1]) == [8]
