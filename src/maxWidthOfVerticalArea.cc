// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

#include <algorithm>
#include <cassert>
#include <math.h>
#include <vector>
using namespace std;

class Solution {
  public:
    int maxWidthOfVerticalArea(vector<vector<int>> &points) {
        // Get x-coords, sort them, return smallest diff

        sort(points.begin(), points.end());
        int max_diff = 0;
        for (int i = 0; i < points.size() - 1; i++) {
            max_diff = max(max_diff, points[i + 1][0] - points[i][0]);
        }
        return max_diff;
    }
};

int main() {
    Solution s;
    vector<vector<int>> p1 = {{8, 7}, {9, 9}, {7, 4}, {9, 7}};
    assert(s.maxWidthOfVerticalArea(p1) == 1);

    vector<vector<int>> p2 = {{3, 1}, {9, 0}, {1, 0}, {1, 4}, {5, 3}, {8, 8}};
    assert(s.maxWidthOfVerticalArea(p2) == 3);

    return 0;
}