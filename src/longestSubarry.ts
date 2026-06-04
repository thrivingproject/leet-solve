export function longestSubarray(nums: number[]): number {
    let zeros: number[] = []
    const notOnes = 2;

    for (let index = 0; index < nums.length; index++) {
        if (nums[index] == 0) {
            zeros.push(index);
        }
    }

    if (zeros.length <= 1) {
        return nums.length - 1;
    } else if (zeros.length == nums.length) {
        return 0;
    }

    let max = Math.max(zeros[0], nums.length - zeros[zeros.length - 1] - 1)

    for (let index = 0; index < zeros.length; index++) {
        if (index == 0) {
            max = Math.max(max, zeros[1] - 1);
        } else if (index == zeros.length - 1) {
            max = Math.max(max, nums.length - zeros[index - 1] - notOnes);
        } else {
            max = Math.max(max, zeros[index + 1] - zeros[index - 1] - notOnes)
        }
    }
    return max;
};