class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        lo = 0
        hi = len(s)
        perm = []
        for char in s:
            if char == "I":
                perm.append(lo)
                lo += 1
            else:
                perm.append(hi)
                hi -= 1
        perm.append(lo)

        return perm
