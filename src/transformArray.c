
#include <stdio.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *transformArray(int *nums, int numsSize, int *returnSize) {
    *returnSize = numsSize;
    int *array = (int *)malloc(sizeof(int) * numsSize);
    int zeroes = 0;
    int i;

    for (i = 0; i < numsSize; i++) {
        if (nums[i] % 2 == 0)
            zeroes++;
    }

    i = 0;
    for (; i < zeroes; i++) {
        *(array + i) = 0;
    }
    for (; i < numsSize; i++) {
        *(array + i) = 1;
    }
    return array;
}

int main(void) {
    int size;
    int nums1[] = {4, 3, 2, 1};
    int *r1 = transformArray(nums1, 4, &size);
    for (int i = 0; i < size; i++)
        printf("%d ", r1[i]);
    printf("\n");

    int nums2[] = {1, 5, 1, 4, 2};
    int *r2 = transformArray(nums2, 5, &size);
    for (int i = 0; i < size; i++)
        printf("%d ", r2[i]);
    printf("\n");
}