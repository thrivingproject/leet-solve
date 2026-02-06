// 66
#include <cassert>
#include <cstdlib>
#include <vector>
using namespace std;

class Solution {
  public:
    vector<int> plusOne(vector<int> &digits) {
        int n, carry;
        n = digits.size();
        div_t divmod;
        vector<int> solution(n);

        n--;
        carry = 1;
        while (n >= 0) {
            divmod = div(digits[n] + carry, 10);
            carry = divmod.quot;
            solution[n] = divmod.rem;
            n--;
        }
        if (carry) {
            solution.insert(solution.begin(), 1);
        }

        return solution;
    }
};

int main() {
    Solution s;

    // Example 1: [1,2,3] -> [1,2,4]
    vector<int> d1 = {1, 2, 3};
    assert((s.plusOne(d1) == vector<int>{1, 2, 4}));

    // Example 2: [4,3,2,1] -> [4,3,2,2]
    vector<int> d2 = {4, 3, 2, 1};
    assert((s.plusOne(d2) == vector<int>{4, 3, 2, 2}));

    // Example 3: [9] -> [1,0]
    vector<int> d3 = {9};
    assert((s.plusOne(d3) == vector<int>{1, 0}));

    printf("All test cases passed!\n");
    return 0;
}