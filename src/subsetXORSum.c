#include <stdio.h>

/**
 * https://leetcode.com/problems/sum-of-all-subset-xor-totals/
 *
 * @param nums
 * @param numsSize
 * @return int
 */
int subsetXORSum(int *nums, int numsSize) {
    int subset_mask, subset_sum;
    int xor_sum = 0;
    int n_sets = 1 << numsSize; // 2^numsSize
    for (subset_mask = 0; subset_mask < n_sets; subset_mask++) {
        subset_sum = 0;
        for (int i = 0; i < numsSize; i++) {
            if (subset_mask & (1 << i)) {
                // nums[i] belongs in subset
                subset_sum ^= nums[i];
            }
        }
        xor_sum += subset_sum;
    }
    return xor_sum;
};

int main(void) {
    // Example 1: nums = [1,3], expected = 6
    int nums1[] = {1, 3};
    int result1 = subsetXORSum(nums1, 2);
    printf("Test 1: %s (got %d, expected 6)\n", result1 == 6 ? "PASS" : "FAIL", result1);

    // Example 2: nums = [5,1,6], expected = 28
    int nums2[] = {5, 1, 6};
    int result2 = subsetXORSum(nums2, 3);
    printf("Test 2: %s (got %d, expected 28)\n", result2 == 28 ? "PASS" : "FAIL", result2);

    // Example 3: nums = [3,4,5,6,7,8], expected = 480
    int nums3[] = {3, 4, 5, 6, 7, 8};
    int result3 = subsetXORSum(nums3, 6);
    printf("Test 3: %s (got %d, expected 480)\n", result3 == 480 ? "PASS" : "FAIL", result3);

    // Edge case: single element
    int nums4[] = {7};
    int result4 = subsetXORSum(nums4, 1);
    printf("Test 4: %s (got %d, expected 7)\n", result4 == 7 ? "PASS" : "FAIL", result4);

    return 0;
}