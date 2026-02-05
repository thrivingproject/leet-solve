// https://leetcode.com/problems/running-sum-of-1d-array/

#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    vector<int> runningSum(vector<int> &nums) {
        vector<int> solution;
        int running = 0;
        for (auto num : nums) {
            solution.push_back(running + num);
            running += num;
        }
        return solution;
    }
};

int main() {
    Solution s;
    vector<int> v1 = {1, 2, 3, 4};
    assert(s.runningSum(v1) == vector<int>({1, 3, 6, 10}));

    vector<int> v2 = {1, 1, 1, 1, 1};
    assert(s.runningSum(v2) == vector<int>({1, 2, 3, 4, 5}));

    vector<int> v3 = {3, 1, 2, 10, 1};
    assert(s.runningSum(v3) == vector<int>({3, 4, 6, 16, 17}));

    cout << "tests passed" << endl;

    return 0;
}