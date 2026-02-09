/**
 * Walk both strings from their last character (LSB) toward the front,
 * summing corresponding digits plus a carry. Build the result string
 * in reverse, then reverse it at the end.
 *
 * Time:  O(max(n, m))  — single pass over the longer string
 * Space: O(max(n, m))  — for the result string
 */

#include <stdlib.h>
#include <string.h>

char *addBinary(char *a, char *b) {
    int la = strlen(a);                   // O(n)
    int lb = strlen(b);                   // O(m)
    int maxLen = (la > lb ? la : lb) + 1; // +1 for possible leading carry

    char *solution = malloc(maxLen + 1); // +1 for null terminator
    int idx = 0;
    int carry = 0;
    int i = la - 1;
    int j = lb - 1;

    // O(max(n, m)) — process digits from LSB to MSB
    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0)
            sum += a[i--] - '0';
        if (j >= 0)
            sum += b[j--] - '0';
        solution[idx++] = (sum % 2) + '0';
        carry = sum / 2;
    }

    solution[idx] = '\0';

    // Reverse the result string in place — O(max(n, m))
    for (int l = 0, r = idx - 1; l < r; l++, r--) {
        char tmp = solution[l];
        solution[l] = solution[r];
        solution[r] = tmp;
    }

    return solution;
}

#include <assert.h>
#include <stdio.h>

int main() {
    char *r1 = addBinary("11", "1");
    assert(strcmp(r1, "100") == 0);
    free(r1);

    char *r2 = addBinary("1010", "1011");
    assert(strcmp(r2, "10101") == 0);
    free(r2);

    printf("All test cases passed!\n");
    return 0;
}