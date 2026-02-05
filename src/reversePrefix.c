/* 3794 */

#include <stdio.h>

char *reversePrefix(char *s, int k) {
    /* Reverse the first k characters of s in-place and return the string. */
    int left = 0;
    int right = k - 1;

    while (left < right) {
        char temp = s[left];
        s[left] = s[right];
        s[right] = temp;
        left++;
        right--;
    }

    return s;
}

void test() {
    char s1[] = "abcd";
    char s2[] = "xyz";
    char s3[] = "hey";

    printf("%s\n", reversePrefix(s1, 2)); /* Expected: bacd */
    printf("%s\n", reversePrefix(s2, 3)); /* Expected: zyx */
    printf("%s\n", reversePrefix(s3, 1)); /* Expected: hey */
}

int main() {
    test();
    return 0;
}
