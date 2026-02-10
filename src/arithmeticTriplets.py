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
