# 1332. Remove Palindromic Subsequences
from src.removePalindromeSub import Solution

s = Solution()


def test_removePalindromeSub_example1():
    assert s.removePalindromeSub("ababa") == 1


def test_removePalindromeSub_example2():
    assert s.removePalindromeSub("abb") == 2


def test_removePalindromeSub_example3():
    assert s.removePalindromeSub("baabb") == 2
