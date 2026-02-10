from src.countSubarrays import Solution

s = Solution()


def test_example1():
    assert s.countSubarrays([1, 3, 2], 4) == 5


def test_example2():
    assert s.countSubarrays([5, 5, 5, 5], 0) == 10


def test_example3():
    assert s.countSubarrays([1, 2, 3], 0) == 3
