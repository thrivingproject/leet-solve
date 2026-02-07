/**
 * Return number of unique triplets (i, j, k) where:
 * -  i < j < k
 * - nums[j] - nums[i] == diff
 * - nums[k] - nums[j] == diff
 * 
 * @param nums 
 * @param diff 
 */
function arithmeticTriplets(nums: number[], diff: number): number {
    let set = new Set();

    for (let i = 0; i < nums.length - 2; i++) {
        for (let j = i + 1; j < nums.length - 1; j++) {
            for (let k = j + 1; k < nums.length; k++) {
                if (nums[j]! - nums[i]! == diff && nums[k]! - nums[j]! == diff) {
                    set.add([i, j, k])
                }
            }
        }
    }

    return set.size;
};

// @ts-ignore
import assert from "node:assert";
assert.strictEqual(arithmeticTriplets([0, 1, 4, 6, 7, 10], 3), 2);
assert.strictEqual(arithmeticTriplets([4, 5, 6, 7, 8, 9], 2), 2);
console.log("All test cases passed!");