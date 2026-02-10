from src.countKConstraintSubstrings import Solution

s = Solution()


def test_example1():
    assert s.countKConstraintSubstrings("10101", 1) == 12


def test_example2():
    assert s.countKConstraintSubstrings("1010101", 2) == 25


def test_example3():
    assert s.countKConstraintSubstrings("11111", 1) == 15
