from src.longestOnes import Solution

s = Solution()


def test_example1():
    assert s.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6


def test_example2():
    assert (
        s.longestOnes(
            [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3
        )
        == 10
    )
