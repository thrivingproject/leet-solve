from src.longestCommonPrefix import Solution

s = Solution()


def test_example1():
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"


def test_example2():
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""
