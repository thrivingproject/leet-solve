class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        s = set()
        for bulb in bulbs:
            if bulb in s:
                s.remove(bulb)
            else:
                s.add(bulb)
        l = list(s)
        l.sort()
        return l
