class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        lt = []
        gt = []
        eq = 0
        for num in nums:
            if num < pivot:
                lt.append(num)
            elif num > pivot:
                gt.append(num)
            else:
                eq += 1

        return lt + [pivot] * eq + gt
