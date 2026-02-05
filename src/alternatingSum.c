/**
 * 3701
 *
 * @param nums
 * @param numsSize
 * @return int
 */
int alternatingSum(int *nums, int numsSize) {
    int sum = 0;
    for (int i = 0; i < numsSize; i++) {
        int num = *(nums + i);
        if (i % 2 == 0) {
            sum += num;
        } else {
            sum -= num;
        }
    }
    return sum;
}