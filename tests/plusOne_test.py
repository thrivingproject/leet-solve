from src.plusOne import Solution

s = Solution()


def test_example1():
    assert s.plusOne([1, 2, 3]) == [1, 2, 4]


def test_example2():
    assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]


def test_example3():
    assert s.plusOne([9]) == [1, 0]
