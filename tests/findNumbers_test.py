from src.findNumbers import Solution

s = Solution()


def test_example1():
    assert s.findNumbers([12, 345, 2, 6, 7896]) == 2


def test_example2():
    assert s.findNumbers([555, 901, 482, 1771]) == 1
