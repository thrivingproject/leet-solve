from src.reverseSubmatrix import Solution

s = Solution()


def test_1():
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
    ]
    assert s.reverseSubmatrix(grid, x=1, y=0, k=3) == [
        [1, 2, 3, 4],
        [13, 14, 15, 8],
        [9, 10, 11, 12],
        [5, 6, 7, 16],
    ]


def test_2():
    grid = [[3, 4, 2, 3], [2, 3, 4, 2]]
    assert s.reverseSubmatrix(grid, x=0, y=2, k=2) == [
        [3, 4, 4, 2],
        [2, 3, 2, 3],
    ]
