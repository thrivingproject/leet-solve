// 1295
#include <assert.h>
#include <stdio.h>

/**
 * Count how many numbers in the array have an even number of digits.
 *
 * For each number, repeatedly divide by 10 to count its digits.
 * If the digit count is even, increment the result.
 *
 * @param nums      Array of non-negative integers.
 * @param numsSize  Length of the nums array.
 * @return          The count of numbers with an even number of digits.
 */
int findNumbers(int *nums, int numsSize) {
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        int digits = 0;
        int n = nums[i];
        while (n > 0) {
            digits++;
            n /= 10;
        }
        if (digits % 2 == 0)
            count++;
    }
    return count;
}

int main(void) {
    int a[] = {12, 345, 2, 6, 7896};
    assert(findNumbers(a, 5) == 2);
    int b[] = {555, 901, 482, 1771};
    assert(findNumbers(b, 4) == 1);
    printf("All test cases passed!\n");
    return 0;
}
