import assert from "node:assert";

/**
 * Find longest subsequence where diff between max and min is exactly 1
 * 
 * A subsequence is an array that can be derived from another array
 * by deleting some or no elements without changing the order of
 * the remaining elements.
 * 
 * @param nums array of nums
 */
function findLHS(nums: number[]): number {
    let ans = 0;
    nums.sort((a, b) => a - b);
    let lo = 0, hi = 1;

    while (hi < nums.length) {
        let min = nums[lo], max = nums[hi];
        while (min == max && hi < nums.length) {
            hi += 1;
            min = nums[lo];
            max = nums[hi];
        }

        if (Math.abs(Math.abs(nums[hi]) - Math.abs(nums[lo])) != 1) {
            while (nums[lo] == min) {
                lo += 1;
            }
        } else {
            ans = Math.max(ans, hi - lo + 1);
        }

        hi += 1;
    }
    return ans;
};

assert(findLHS([10, 5, 6, 5, 8, 2, 1, 0, 4, 4, 1, 9, 8, 5, 7, 7, 8, 10, 8, 10, 5, 0, 7, 9, 10, 6, 2, 2, 9, 4, 10, 7, 2, 10, 7, 3, 4, 9, 2, 0, 5, 9, 4, 9, 5, 2, 0, 3, 7, 7, 4, 10, 7, 9, 4, -10, 3, 8, 5, 10, 6, 4, 3, 2, 0, 7, 6, 10, 6, 8, 4, 1, 8, 9]) === 17);
assert(findLHS([1, 1, 1, 1, 1, 1, 3, 5, 5, 6]) === 3);
assert(findLHS([-1, -1, -1, -1, 0, 0, 0]) === 7);
assert(findLHS([-1, 0, -1, 0, -1, 0, -1]) === 7);
assert(findLHS([-3, -3, -2, -1, -1, -1]) === 4);
assert(findLHS([-3, -1, -1, -1, -3, -2]) === 4);
assert(findLHS([1, 3, 2, 2, 5, 2, 3, 7]) === 5);
assert(findLHS([1, 2, 2, 2, 3, 3, 5, 7]) === 5);
assert(findLHS([1, 2, 3, 4]) === 2);
assert(findLHS([1, 1, 1, 1]) === 0);
assert(findLHS([1, 1, 2, 2]) === 4);
assert(findLHS([1, 2, 2, 1]) === 4);
