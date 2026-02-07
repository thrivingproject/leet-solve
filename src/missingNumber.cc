// 268. Missing Number
#include <algorithm>
#include <cassert>
#include <vector>
using namespace std;

class Solution {
  public:
    /**
     * This is O(n log n) since cpp sort is O(n log n) and 1 iteration is O(n)
     *
     * @param nums
     * @return int
     */
    int missingNumber(vector<int> &nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            if (i != nums[i]) {
                return i;
            }
        }
        return n;
    }

    /**
     * Since all numbers should be in array, expected sum is
     * 1 + 2 + ... n. We can take the actual sum and subtract
     * the expected sum to get the missing number.
     *
     * @param nums
     * @return int
     */
    int missingNumberOptimal(vector<int> &nums) {
        int n = nums.size();
        // Set to n initially since we don't add n in loop
        int expected_sum = n;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            expected_sum += i;
        }
        return expected_sum - sum;
    }
};

int main() {
    Solution s;

    // Example 1: nums = [3,0,1] -> 2
    vector<int> v1 = {3, 0, 1};
    assert(s.missingNumberOptimal(v1) == 2);

    // Example 2: nums = [0,1] -> 2
    vector<int> v2 = {0, 1};
    assert(s.missingNumberOptimal(v2) == 2);

    // Example 3: nums = [9,6,4,2,3,5,7,0,1] -> 8
    vector<int> v3 = {9, 6, 4, 2, 3, 5, 7, 0, 1};
    assert(s.missingNumberOptimal(v3) == 8);

    printf("All test cases passed!\n");
    return 0;
}