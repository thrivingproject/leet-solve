// 4. Median of Two Sorted Arrays
#include <cassert>
#include <cstdio>
#include <vector>
using namespace std;

class Solution {
  public:
    /**
     * Solution sorts arrays and then gets median. Time complexity O(n log n).
     * Not optimal since optimal solution problems states complexity must be
     * O(log(m+n)).
     *
     * @param nums1
     * @param nums2
     * @return double
     */
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) {
        vector<int> solution;
        int m, n, solution_size;
        int nums1_i, nums2_i, solution_i;
        int num_1, num_2;

        m = nums1.size();
        n = nums2.size();
        solution_size = m + n;
        solution_i = solution_size / 2;

        nums1_i = 0, nums2_i = 0;
        while (nums1_i < m && nums2_i < n) {
            num_1 = nums1[nums1_i];
            num_2 = nums2[nums2_i];
            if (num_1 > num_2) {
                solution.push_back(num_2);
                nums2_i++;
            } else {
                solution.push_back(num_1);
                nums1_i++;
            }
        }
        while (nums1_i < m) {
            solution.push_back(nums1[nums1_i++]);
        }
        while (nums2_i < n) {
            solution.push_back(nums2[nums2_i++]);
        }

        if (solution_size % 2 == 0) {
            return (solution[solution_i] + solution[solution_i - 1]) / 2.0;
        } else {
            return solution[solution_i];
        }
    }
};

int main() {
    Solution s;

    // Example 1: nums1 = [1,3], nums2 = [2] -> 2.0
    vector<int> n1 = {1, 3}, n2 = {2};
    assert(s.findMedianSortedArrays(n1, n2) == 2.0);

    // Example 2: nums1 = [1,2], nums2 = [3,4] -> 2.5
    vector<int> n3 = {1, 2}, n4 = {3, 4};
    assert(s.findMedianSortedArrays(n3, n4) == 2.5);

    printf("All test cases passed!\n");
    return 0;
}