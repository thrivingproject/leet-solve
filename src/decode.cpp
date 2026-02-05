#include <cassert>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
  public:
    vector<int> decode(vector<int> &encoded, int first) {
        vector<int> solution;
        solution.push_back(first);

        for (int i = 0; i < encoded.size(); i++) {

            // solution[i] xor solution[i + 1] = encoded[i]
            // encoded[i] xor solution[i] = solution[i] xor solution[i + 1] xor
            // solution[i] = solution[i + 1]
            solution.push_back(encoded[i] ^ solution[i]);
        }

        return solution;
    }
};

int main() {
    Solution s;

    vector<int> e1 = {1, 2, 3};
    assert(s.decode(e1, 1) == vector<int>({1, 0, 2, 1}));

    vector<int> e2 = {6, 2, 7, 3};
    assert(s.decode(e2, 4) == vector<int>({4, 2, 0, 7, 4}));

    cout << "tests passed" << endl;
}