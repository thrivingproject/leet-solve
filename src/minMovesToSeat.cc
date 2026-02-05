// 2037

#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    int minMovesToSeat(vector<int> &seats, vector<int> &students) {
        int moves = 0;

        // Sort the arrays, get sum of element-wise subtraction
        sort(seats.begin(), seats.end());
        sort(students.begin(), students.end());

        for (int i = 0; i < seats.size(); i++) {
            moves += abs(seats[i] - students[i]);
        }

        return moves;
    }
};

int main() {
    Solution s;

    vector<int> seats1 = {3, 1, 5}, students1 = {2, 7, 4};
    assert(s.minMovesToSeat(seats1, students1) == 4);

    vector<int> seats2 = {4, 1, 5, 9}, students2 = {1, 3, 2, 6};
    assert(s.minMovesToSeat(seats2, students2) == 7);

    vector<int> seats3 = {2, 2, 6, 6}, students3 = {1, 3, 2, 6};
    assert(s.minMovesToSeat(seats3, students3) == 4);

    cout << "All test cases passed!" << endl;

    return 0;
}