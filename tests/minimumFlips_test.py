# 3750. Minimum Number of Flips to Make Binary String Equal to Its Reverse
from src.minimumFlips import Solution

s = Solution()


def test_example1():
    assert s.minimumFlips(7) == 0


def test_example2():
    assert s.minimumFlips(10) == 4
