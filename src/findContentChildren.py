class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        happy = 0
        gi = si = 0
        while gi < len(g) and si < len(s):
            greed = g[gi]
            size = s[si]
            if greed <= size:
                happy += 1
                gi += 1
                si += 1
            else:
                si += 1
        return happy
