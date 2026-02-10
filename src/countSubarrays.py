class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """#TODO optimize."""
        count = 0
        size = len(nums)
        nums_sets = dict()

        for l in range(size):
            for r in range(l, size):
                sub_set = tuple(nums[l : r + 1])

                if sub_set in nums_sets:
                    if nums_sets[sub_set] <= k:
                        count += 1
                    continue

                cost = (max(sub_set) - min(sub_set)) * (r - l + 1)
                nums_sets[sub_set] = cost
                if cost <= k:
                    count += 1
        return count
