class Solution:
    def findTheDistanceValue(
        self, arr1: list[int], arr2: list[int], d: int
    ) -> int:
        count = 0
        arr2.sort()

        for num in arr1:
            works = True
            l = 0
            r = len(arr2) - 1
            while l <= r and works:
                mid = (r + l) // 2
                if abs(num - arr2[mid]) <= d:
                    works = False
                elif num < arr2[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            if works:
                count += 1

        return count
