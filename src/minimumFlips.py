class Solution:
    def minimumFlips(self, n: int) -> int:
        n_bin = bin(n)[2:]
        n_bin_rev = n_bin[::-1]
        count = 0
        for a, b in zip(n_bin, n_bin_rev):
            if a != b:
                count += 1
        return count

    def minimumFlipsTwoPointer(self, n: int) -> int:
        n_bin = bin(n)[2:]
        l, r = 0, len(n_bin) - 1
        count = 0
        while l < r:
            if n_bin[l] != n_bin[r]:
                count += 2
            l += 1
            r -= 1
        return count
