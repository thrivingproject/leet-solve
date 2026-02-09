// 557. Reverse Words in a String III
#include <assert.h>
#include <stdio.h>
#include <string.h>

char *reverseWords(char *s) {
    int start = 0;
    int len = strlen(s);

    for (int i = 0; i <= len; i++) {
        // End of word
        if (i == len || s[i] == ' ') {
            // Reverse the word
            int left = start, right = i - 1;
            while (left < right) {
                char tmp = s[left];
                s[left++] = s[right];
                s[right--] = tmp;
            }
            // Mark start of new word
            start = i + 1;
        }
    }
    return s;
}

int main(void) {
    char s1[] = "Let's take LeetCode contest";
    assert(strcmp(reverseWords(s1), "s'teL ekat edoCteeL tsetnoc") == 0);

    char s2[] = "Mr Ding";
    assert(strcmp(reverseWords(s2), "rM gniD") == 0);

    printf("All test cases passed!\n");
    return 0;
}
