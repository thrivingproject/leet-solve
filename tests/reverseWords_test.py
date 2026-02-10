from src.reverseWords import Solution

s = Solution()


def test_example1():
    assert (
        s.reverseWords("Let's take LeetCode contest")
        == "s'teL ekat edoCteeL tsetnoc"
    )


def test_example2():
    assert s.reverseWords("Mr Ding") == "rM gniD"
