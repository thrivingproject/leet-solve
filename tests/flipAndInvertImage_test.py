# 832. Flipping an Image
from src.flipAndInvertImage import Solution

s = Solution()


def test_example1():
    assert s.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]) == [
        [1, 0, 0],
        [0, 1, 0],
        [1, 1, 1],
    ]


def test_example2():
    assert s.flipAndInvertImage(
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    ) == [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]
