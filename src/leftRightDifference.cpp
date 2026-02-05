// https://leetcode.com/problems/left-and-right-sum-differences/

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

int *leftRightDifference(int *nums, int numsSize, int *returnSize) {
    int *array = (int *)malloc(sizeof(int) * numsSize);
    int rightsum[numsSize];
    int i, last;

    last = 0;
    for (i = numsSize - 1; i >= 0; i--) {
        rightsum[i] = last;
        last += nums[i];
    }
    last = 0;
    for (i = 0; i < numsSize; i++) {
        *(array + i) = abs(last - rightsum[i]);
        last += nums[i];
    }

    *returnSize = numsSize;
    return array;
}

int main() {
    int returnSize;
    int *result;

    // Test 1: [10,4,8,3] -> [15,1,11,22]
    int nums1[] = {10, 4, 8, 3};
    result = leftRightDifference(nums1, 4, &returnSize);
    assert(returnSize == 4);
    assert(result[0] == 15 && result[1] == 1 && result[2] == 11 &&
           result[3] == 22);
    free(result);

    // Test 2: [1] -> [0]
    int nums2[] = {1};
    result = leftRightDifference(nums2, 1, &returnSize);
    assert(returnSize == 1);
    assert(result[0] == 0);
    free(result);

    printf("All tests passed\n");
    return 0;
}