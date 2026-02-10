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
