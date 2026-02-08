class Solution:
    def mergeAdjacent(self, nums: list[int]) -> list[int]:
        solution = [nums[0]]
        ptr = 1
        size = len(nums)
        while ptr < size:
            if nums[ptr] == solution[-1]:
                solution[-1] *= 2
                while len(solution) > 1 and solution[-1] == solution[-2]:
                    solution[-2] *= 2
                    solution.pop()
            else:
                solution.append(nums[ptr])
            ptr += 1
        return solution


# Tests
s = Solution()
assert s.mergeAdjacent([3, 1, 1, 2]) == [3, 4]
assert s.mergeAdjacent([2, 2, 4]) == [8]
assert s.mergeAdjacent([3, 7, 5]) == [3, 7, 5]
assert s.mergeAdjacent([2, 1, 1, 2]) == [4, 2]
assert s.mergeAdjacent([4, 2, 1, 1]) == [8]
print("All test cases passed!")
