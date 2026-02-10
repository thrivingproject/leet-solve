from src.addBinary import Solution

s = Solution()


def test_example1():
    assert s.addBinary("11", "1") == "100"


def test_example2():
    assert s.addBinary("1010", "1011") == "10101"
