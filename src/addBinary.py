"""
Walk both strings from their last character (LSB) toward the front,
summing corresponding digits plus a carry. Build the result in reverse,
then reverse it at the end.

Time:  O(max(n, m)) — single pass over the longer string
Space: O(max(n, m)) — for the result string

list.append is backed by a contiguous array, so it's more cache-friendly and has lower constant overhead than deque.appendleft (which uses a doubly-linked block structure).
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        # O(max(n, m)) — process digits from LSB to MSB
        while i >= 0 or j >= 0 or carry:
            _sum = carry
            if i >= 0:
                _sum += int(a[i])
                i -= 1
            if j >= 0:
                _sum += int(b[j])
                j -= 1
            result.append(str(_sum % 2))
            carry = _sum // 2

        return "".join(reversed(result))  # O(max(n, m))


sol = Solution()

assert sol.addBinary("11", "1") == "100"
assert sol.addBinary("1010", "1011") == "10101"

print("All test cases passed!")
