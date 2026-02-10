"""
Traverse digits right to left, adding 1 (the carry).
If a digit becomes 10, set it to 0 and continue carrying.
If carry remains after processing all digits, prepend 1.
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # O(n) - single right-to-left pass
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0  # carry
                continue
            else:
                digits[i] += 1  # no carry, done
                return digits

        return [1] + digits
