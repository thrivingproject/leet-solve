class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""

    def firstPalindromeTwoPointer(self, words: list[str]) -> str:
        for word in words:
            left, right = 0, len(word) - 1
            while left < right:
                if word[left] != word[right]:
                    break
                left += 1
                right -= 1
            else:
                return word
        return ""


# 2108. Find First Palindromic String in the Array
s = Solution()
assert s.firstPalindrome(["abc", "car", "ada", "racecar", "cool"]) == "ada"
assert s.firstPalindrome(["notapalindrome", "racecar"]) == "racecar"
assert s.firstPalindrome(["def", "ghi"]) == ""
assert (
    s.firstPalindromeTwoPointer(["abc", "car", "ada", "racecar", "cool"])
    == "ada"
)
assert s.firstPalindromeTwoPointer(["notapalindrome", "racecar"]) == "racecar"
assert s.firstPalindromeTwoPointer(["def", "ghi"]) == ""
print("All test cases passed!")
