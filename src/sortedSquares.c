// 977. Squares of a Sorted Array
#include <stdlib.h>

int *sortedSquares(int *nums, int numsSize, int *returnSize) {
    *returnSize = numsSize;
    int *squares = (int *)malloc(numsSize * sizeof(int));
    int l = 0, r = numsSize - 1;
    for (int i = r; i >= 0; i--) {
        if (abs(nums[r]) > abs(nums[l])) {
            squares[i] = nums[r] * nums[r];
            r--;
        } else {
            squares[i] = nums[l] * nums[l];
            l++;
        }
    }
    return squares;
}
