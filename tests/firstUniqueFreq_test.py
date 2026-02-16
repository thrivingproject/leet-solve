from src.firstUniqueFreq import Solution

s = Solution()


def test_1():
    nums = [20, 10, 30, 30]
    out = 30
    assert s.firstUniqueFreq(nums) == out


def test_2():
    nums = [20, 20, 10, 30, 30, 30]
    out = 20
    assert s.firstUniqueFreq(nums) == out
