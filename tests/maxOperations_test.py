from src.maxOperations import Solution

s = Solution()


def test_example1():
    assert s.maxOperations([1, 2, 3, 4], 5) == 2


def test_example2():
    assert s.maxOperations([3, 1, 3, 4, 3], 6) == 1
