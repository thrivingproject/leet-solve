class Solution:
    def almostPalindromic(self, s: str) -> int:
        n = len(s)
        for length in range(n, 0, -1):
            for i in range(n - length + 1):
                l, r = i, i + length - 1
                while l < r and s[l] == s[r]:
                    l += 1
                    r -= 1
                if l >= r:
                    return length
                s1 = s[l + 1:r + 1]
                s2 = s[l:r]
                if s1 == s1[::-1] or s2 == s2[::-1]:
                    return length
        return 0
