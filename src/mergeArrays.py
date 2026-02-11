class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        nums2_ptr = 0
        solution = []
        for arr in nums1:
            while nums2_ptr < len(nums2) and nums2[nums2_ptr][0] < arr[0]:
                solution.append(nums2[nums2_ptr])
                nums2_ptr += 1
            if nums2_ptr < len(nums2) and arr[0] == nums2[nums2_ptr][0]:
                solution.append([arr[0], arr[1] + nums2[nums2_ptr][1]])
                nums2_ptr += 1
            else:
                solution.append(arr)
        while nums2_ptr < len(nums2):
            solution.append(nums2[nums2_ptr])
            nums2_ptr += 1

        return solution
