from src.dominantIndecies import Solution

s = Solution()


def test_example1():
    assert s.dominantIndices([5, 4, 3]) == 2


def test_example2():
    assert s.dominantIndices([4, 1, 2]) == 1
