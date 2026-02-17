from src.isPrefixOfWord import Solution

s = Solution()

def test_1():
    assert s.isPrefixOfWord("i love eating burger", "burg") == 4

def test_2():
    assert s.isPrefixOfWord("this problem is an easy problem", "pro") == 2

def test_3():
    assert s.isPrefixOfWord("i am tired", "you") == -1
