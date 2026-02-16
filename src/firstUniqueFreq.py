class Solution:
    def firstUniqueFreq(self, nums: list[int]) -> int:
        d = {}
        d2 = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for num, freq in d.items():
            d2[freq] = d2.get(freq, 0) + 1
        unique_freq = 0
        for k, v in d2.items():
            if v == 1:
                unique_freq = k
                break

        for k, v in d.items():
            if v == unique_freq:
                return k
        return -1
