from src.minOperations import Solution

s = Solution()


def test_example1():
    assert s.minOperations([0, 1, 1, 1, 0, 0]) == 3


def test_example2():
    assert s.minOperations([0, 1, 1, 1]) == -1
