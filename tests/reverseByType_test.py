# Reverse By Type
from src.reverseByType import Solution

s = Solution()


def test_example1():
    assert s.reverseByType(")ebc#da@f(") == "(fad@cb#e)"


def test_example2():
    assert s.reverseByType("z") == "z"


def test_example3():
    assert s.reverseByType("!@#$%^&*()") == ")(*&^%$#@!"
