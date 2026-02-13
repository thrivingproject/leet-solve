from src.shortestToChar import Solution

s = Solution()


def test_1():
    assert s.shortestToChar(s="loveleetcode", c="e") == [
        3,
        2,
        1,
        0,
        1,
        0,
        0,
        1,
        2,
        2,
        1,
        0,
    ]


def test_2():
    assert s.shortestToChar("aaab", "b") == [3, 2, 1, 0]


def test_3():
    assert s.shortestToChar("cizokxcijwbyspcfcqws", "c") == [
        0,
        1,
        2,
        3,
        2,
        1,
        0,
        1,
        2,
        3,
        4,
        3,
        2,
        1,
        0,
        1,
        0,
        1,
        2,
        3,
    ]
