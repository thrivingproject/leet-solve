# 2697. Lexicographically Smallest Palindrome
from src.makeSmallestPalindrome import Solution

s = Solution()


def test_example1():
    assert s.makeSmallestPalindrome("egcfe") == "efcfe"


def test_example2():
    assert s.makeSmallestPalindrome("abcd") == "abba"


def test_example3():
    assert s.makeSmallestPalindrome("seven") == "neven"
