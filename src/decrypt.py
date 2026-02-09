"""
1652. Defuse the Bomb

Sliding Window

Given a circular array `code` of length n and an integer k:
- If k > 0, replace each element with the sum of the next k elements.
- If k < 0, replace each element with the sum of the previous |k| elements.
- If k == 0, replace every element with 0.

Use a sliding window of size |k| over the circular array. Compute the
initial window sum, then slide by adding the next element and removing
the trailing element, using modular indexing to wrap around.

Time Complexity: O(n) — one pass to initialize the window, one pass to slide.
Space Complexity: O(n) — for the output array.
"""


class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        size = len(code)
        if k == 0:
            return [0] * size

        nums = []
        s = 0
        rev = False
        if k < 0:
            rev = True
            k *= -1
            code.reverse()
        for i in range(1, k + 1):
            s += code[i % (k + 1)]
        nums.append(s)
        for i in range(1, size):
            s -= code[i]
            s += code[(i + k) % size]
            nums.append(s)
        if rev:
            nums.reverse()
        return nums


sol = Solution()
assert sol.decrypt([5, 7, 1, 4], 3) == [12, 10, 16, 13]
assert sol.decrypt([1, 2, 3, 4], 0) == [0, 0, 0, 0]
assert sol.decrypt([2, 4, 9, 3], -2) == [12, 5, 6, 13]
assert sol.decrypt([5, 2, 2, 3, 1], 3) == [7, 6, 9, 8, 9]

print("All test cases passed!")
