# Tests for findContentChildren (LeetCode 455)
# Problem: Assign Cookies

from src.findContentChildren import Solution

s = Solution()


def test_example1():
    assert s.findContentChildren([1, 2, 3], [1, 1]) == 1


def test_example2():
    assert s.findContentChildren([1, 2], [1, 2, 3]) == 2
