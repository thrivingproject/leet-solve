from src.toggleLightBulbs import Solution

s = Solution()


def test_1():
    bulbs = [10, 30, 20, 10]
    assert s.toggleLightBulbs(bulbs) == [20, 30]


def test_2():
    bulbs = [100, 100]
    assert s.toggleLightBulbs(bulbs) == []
