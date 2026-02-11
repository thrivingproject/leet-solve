class Solution:
    def findKDistantIndices(
        self, nums: list[int], key: int, k: int
    ) -> list[int]:
        output = []
        i = nums.index(key)
        last = 0

        for i in range(len(nums)):
            if nums[i] == key:
                start = max(0, i - k, last)
                stop = min(i + k + 1, len(nums))
                for j in range(start, stop):
                    output.append(j)
                last = stop

        return output
