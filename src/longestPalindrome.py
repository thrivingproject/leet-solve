class Solution:
    def longestPalindrome(self, s: str) -> str:
        best_l = 0
        best_r = 0
        # This only checks for odd numbered palindromes
        for i in range(len(s)):
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) > (best_r - best_l):
                    best_l = l
                    best_r = r
                l -= 1
                r += 1
        # Need to check for even numbered palindromes
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l) > (best_r - best_l):
                    best_l = l
                    best_r = r
                l -= 1
                r += 1
        return s[best_l : best_r + 1]
