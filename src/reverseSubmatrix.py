class Solution:
    def reverseSubmatrix(
        self, grid: list[list[int]], x: int, y: int, k: int
    ) -> list[list[int]]:
        hi = x + k - 1

        while x < hi:
            for i in range(k):
                grid[x][y + i], grid[hi][y + i] = (
                    grid[hi][y + i],
                    grid[x][y + i],
                )
            x += 1
            hi -= 1

        return grid
