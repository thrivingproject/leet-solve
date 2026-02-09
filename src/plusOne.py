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


# Tests
s = Solution()

# Example 1: [1,2,3] -> [1,2,4]
assert s.plusOne([1, 2, 3]) == [1, 2, 4]

# Example 2: [4,3,2,1] -> [4,3,2,2]
assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]

# Example 3: [9] -> [1,0]
assert s.plusOne([9]) == [1, 0]

print("All test cases passed!")
