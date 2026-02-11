# 344. Reverse String
from src.reverseString import Solution

s = Solution()


def test_example1():
    chars = ["h", "e", "l", "l", "o"]
    s.reverseString(chars)
    assert chars == ["o", "l", "l", "e", "h"]


def test_example2():
    chars = ["H", "a", "n", "n", "a", "h"]
    s.reverseString(chars)
    assert chars == ["h", "a", "n", "n", "a", "H"]
