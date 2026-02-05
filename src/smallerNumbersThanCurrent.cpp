#include <algorithm>
#include <cassert>
#include <vector>

using namespace std;

class Solution {
  public:
    vector<int> smallerNumbersThanCurrent(vector<int> &nums) {
        vector<int> sol;
        // Create a sorted copy so we can break out early
        vector<int> sorted = nums;
        sort(sorted.begin(), sorted.end());
        for (int num : nums) {
            int i = 0;
            while (sorted[i] < num)
                i++;
            sol.push_back(i);
        }
        return sol;
    }
};

int main(void) {
    Solution s;
    vector<int> t1 = {8, 1, 2, 2, 3};
    assert(s.smallerNumbersThanCurrent(t1) == vector<int>({4, 0, 1, 1, 3}));
    vector<int> t2 = {6, 5, 4, 8};
    assert(s.smallerNumbersThanCurrent(t2) == vector<int>({2, 1, 0, 3}));
}