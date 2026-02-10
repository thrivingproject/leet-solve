from src.firstPalindrome import Solution

s = Solution()


def test_firstPalindrome_example1():
    assert s.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]) == "ada"


def test_firstPalindrome_example2():
    assert s.firstPalindrome(["notapalindrome", "racecar"]) == "racecar"


def test_firstPalindrome_example3():
    assert s.firstPalindrome(["def", "ghi"]) == ""


def test_firstPalindromeTwoPointer_example1():
    assert (
        s.firstPalindromeTwoPointer(["abc", "car", "ada", "racecar", "cool"])
        == "ada"
    )


def test_firstPalindromeTwoPointer_example2():
    assert s.firstPalindromeTwoPointer(["notapalindrome", "racecar"]) == "racecar"


def test_firstPalindromeTwoPointer_example3():
    assert s.firstPalindromeTwoPointer(["def", "ghi"]) == ""
