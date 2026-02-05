// https://leetcode.com/problems/transformed-array/

#include <cassert>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    vector<int> constructTransformedArray(vector<int> &nums) {
        int n = nums.size();
        vector<int> result(n);

        for (int i = 0; i < n; i++) {
            int num = nums[i];
            if (num > 0) {
                result[i] = nums[(i + num) % n];
            } else if (num < 0) {
                int index = i - abs(num);
                while (index < 0) {
                    index += n;
                }
                result[i] = nums[index];
            } else {
                result[i] = num;
            }
        }
        return result;
    }

    /**
     * Common solution
     *
     * @param nums
     * @return vector<int>
     */
    static vector<int> constructTransformedArray0ms(vector<int> &nums) {
        const int n = nums.size();
        vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            int j = (i + nums[i]) % n;
            ans[i] = nums[j + (-(j < 0) & n)];
        }
        return ans;
    }
};

int main() {
    Solution sol;

    // Example 1: nums = [3,-2,1,1] -> [1,1,1,3]
    vector<int> nums1 = {3, -2, 1, 1};
    vector<int> expected1 = {1, 1, 1, 3};
    assert(sol.constructTransformedArray(nums1) == expected1);

    // Test with single element
    vector<int> nums4 = {-1, 4, -1};
    vector<int> expected4 = {-1, -1, 4};
    assert(sol.constructTransformedArray(nums4) == expected4);

    cout << "All test cases passed!" << endl;
    return 0;
}