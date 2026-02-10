from src.arithmeticTriplets import Solution

s = Solution()


def test_example1():
    assert s.arithmeticTriplets([0, 1, 4, 6, 7, 10], 3) == 2


def test_example2():
    assert s.arithmeticTriplets([4, 5, 6, 7, 8, 9], 2) == 2
