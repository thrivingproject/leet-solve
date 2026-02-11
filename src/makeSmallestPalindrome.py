class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        """Two pointer"""
        out = list(s)
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] < s[r]:
                out[l] = out[r] = s[l]
            else:
                out[l] = out[r] = s[r]
            l += 1
            r -= 1

        return "".join(out)
