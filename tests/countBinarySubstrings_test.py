"""
696. Count Binary Substrings

Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
"""

from src.countBinarySubstrings import Solution

s = Solution()


def test_example1():
    assert s.countBinarySubstrings("00110011") == 6


def test_example2():
    assert s.countBinarySubstrings("10101") == 4


def test_3():
    assert s.countBinarySubstrings("1111") == 0


def test_4():
    assert s.countBinarySubstrings("100111001") == 6
