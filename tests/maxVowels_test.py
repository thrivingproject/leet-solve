from src.maxVowels import Solution

s = Solution()


def test_example1():
    assert s.maxVowels("abciiidef", 3) == 3


def test_example2():
    assert s.maxVowels("aeiou", 2) == 2


def test_example3():
    assert s.maxVowels("leetcode", 3) == 2
