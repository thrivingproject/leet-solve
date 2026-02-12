# 5. Longest Palindromic Substring
from src.longestPalindrome import Solution

s = Solution()


def test_example1():
    assert s.longestPalindrome("babad") in ("bab", "aba")


def test_example2():
    assert s.longestPalindrome("cbbd") == "bb"


def test_example3():
    assert s.longestPalindrome("abb") == "bb"


def test_example4():
    assert s.longestPalindrome("ccd") == "cc"


def test_example5():
    assert s.longestPalindrome("eabcb") == "bcb"


def test_example6():
    assert s.longestPalindrome("ccc") == "ccc"


def test_example7():
    assert s.longestPalindrome("abaab") == "baab"
