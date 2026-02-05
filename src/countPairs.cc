#include <iostream>
#include <vector>

using namespace std;

class Solution {
  public:
    int countPairs(vector<int> &nums, int target) {
        int pairs = 0, n = nums.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] + nums[j] < target) {
                    pairs += 1;
                }
            }
        }

        return pairs;
    }
};

int main() {
    Solution sol;

    // Test 1: nums = [-1,1,2,3,1], target = 2, expected = 3
    vector<int> nums1 = {-1, 1, 2, 3, 1};
    int result1 = sol.countPairs(nums1, 2);
    cout << "Test 1: " << (result1 == 3 ? "PASS" : "FAIL")
         << " (expected 3, got " << result1 << ")" << endl;

    // Test 2: nums = [-6,2,5,-2,-7,-1,3], target = -2, expected = 10
    vector<int> nums2 = {-6, 2, 5, -2, -7, -1, 3};
    int result2 = sol.countPairs(nums2, -2);
    cout << "Test 2: " << (result2 == 10 ? "PASS" : "FAIL")
         << " (expected 10, got " << result2 << ")" << endl;

    return 0;
}