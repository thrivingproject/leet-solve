from src.almostPalindromic import Solution

s = Solution()


def test_1():
    assert s.almostPalindromic("abca") == 4


def test_2():
    assert s.almostPalindromic("abba") == 4


def test_3():
    assert s.almostPalindromic("zzabba") == 5


def test_4():
    assert s.almostPalindromic("aabc") == 3


def test_5():
    assert s.almostPalindromic("bqqbbqbqqqb") == 8
