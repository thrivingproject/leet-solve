# 942. DI String Match
from src.diStringMatch import Solution

s = Solution()


def test_example1():
    assert s.diStringMatch("IDID") == [0, 4, 1, 3, 2]


def test_example2():
    assert s.diStringMatch("III") == [0, 1, 2, 3]


def test_example3():
    assert s.diStringMatch("DDD") == [3, 2, 1, 0]
