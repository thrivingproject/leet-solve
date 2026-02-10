from src.countMaxOrSubsets import Solution

s = Solution()


def test_example1():
    assert s.countMaxOrSubsets([3, 1]) == 2


def test_example2():
    assert s.countMaxOrSubsets([2, 2, 2]) == 7


def test_example3():
    assert s.countMaxOrSubsets([3, 2, 1, 5]) == 6
