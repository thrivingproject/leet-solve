#include <cassert>
#include <vector>
using namespace std;

/**
 * https://leetcode.com/problems/pascals-triangle/description/
 */
class Solution {
  public:
    /**
     * * TODO: optimize (initialize with ones, skip some indices)
     *
     * n items in row = row number (or row number + 1 for 0 index row number)
     * for i in row, if i == 0 or i == row_n_items - 1, row[i] = 1
     */
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> matrix;
        int row_num;

        for (row_num = 0; row_num < numRows; row_num++) {
            // Build the row
            vector<int> row;
            for (int i = 0; i <= row_num; i++) {
                if (i == 0 || i == row_num) {
                    row.push_back(1);
                } else {
                    vector<int> prev_row = matrix.at(row_num - 1);
                    row.push_back(prev_row.at(i - 1) + prev_row.at(i));
                }
            }
            // Append the row to the matrix
            matrix.push_back(row);
        }

        vector<int> row;
        return matrix;
    }
};

int main() {
    Solution s;

    // Example 1: numRows = 5
    vector<vector<int>> result1 = s.generate(5);
    assert(result1[0] == vector<int>({1}));
    assert(result1[1] == (vector<int>{1, 1}));
    assert(result1[2] == (vector<int>{1, 2, 1}));
    assert(result1[3] == (vector<int>{1, 3, 3, 1}));
    assert(result1[4] == (vector<int>{1, 4, 6, 4, 1}));

    // Example 2: numRows = 1
    vector<vector<int>> result2 = s.generate(1);
    assert(result2[0] == vector<int>({1}));

    printf("All test cases passed!\n");
    return 0;
}