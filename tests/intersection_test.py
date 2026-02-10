from src.intersection import Solution

s = Solution()


def test_example1():
    result = s.intersection([1, 2, 2, 1], [2, 2])
    assert sorted(result) == [2]


def test_example2():
    result = s.intersection([4, 9, 5], [9, 4, 9, 8, 4])
    assert sorted(result) == [4, 9]
