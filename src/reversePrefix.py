"""https://leetcode.com/problems/reverse-prefix-of-word/description/"""


class Solution:
    """Supposed to be a two pointer prob but not necessary in Python"""

    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            i = word.index(ch) + 1
        except ValueError:
            return word
        sub_str = word[:i]
        rev_part = sub_str[::-1]
        return rev_part + word[i:]
