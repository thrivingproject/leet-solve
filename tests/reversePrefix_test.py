from src.reversePrefix import Solution

s = Solution()


def test_example1():
    assert s.reversePrefix("abcdefd", "d") == "dcbaefd"


def test_example2():
    assert s.reversePrefix("xyxzxe", "z") == "zxyxxe"


def test_example3():
    assert s.reversePrefix("abcd", "z") == "abcd"
