class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        """
        Return number of unique triplets (i, j, k) where:
        - i < j < k
        - nums[j] - nums[i] == diff
        - nums[k] - nums[j] == diff

        Time complexity is O(n) (creating set, looping over nums)
        """
        nums_set = set(nums)
        count = 0

        for num in nums:
            nums_j = diff + num
            nums_k = diff + nums_j
            if nums_j in nums_set and nums_k in nums_set:
                count += 1

        return count


# 2367. Number of Arithmetic Triplets
s = Solution()

assert s.arithmeticTriplets([0, 1, 4, 6, 7, 10], 3) == 2
assert s.arithmeticTriplets([4, 5, 6, 7, 8, 9], 2) == 2

print("All test cases passed!")
