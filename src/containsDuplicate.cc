#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
  public:
    bool containsDuplicate(vector<int> &nums) {
        /*
         * unordered_set (hash table) vs set (red-black tree):
         *   unordered_set: O(1) avg, O(n) worst (hash collisions/rehashing)
         *   set:           O(log n) always
         * Order doesn't matter here, so unordered_set wins on average case.
         */
        unordered_set<int> nums_set;
        for (int num : nums) {
            if (!nums_set.insert(num).second) {
                return true;
            }
        }
        return false;
    }
};

int main(void) {
    Solution s;

    // Example 1: [1,2,3,1] -> true
    vector<int> nums1 = {1, 2, 3, 1};
    assert(s.containsDuplicate(nums1) == true);

    // Example 2: [1,2,3,4] -> false
    vector<int> nums2 = {1, 2, 3, 4};
    assert(s.containsDuplicate(nums2) == false);

    // Example 3: [1,1,1,3,3,4,3,2,4,2] -> true
    vector<int> nums3 = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
    assert(s.containsDuplicate(nums3) == true);

    cout << "All test cases passed!" << endl;
    return 0;
}