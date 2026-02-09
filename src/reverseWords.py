class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        for word in s.split():
            words.append(word[::-1])
        return " ".join(words)


# 557. Reverse Words in a String III
sol = Solution()
assert (
    sol.reverseWords("Let's take LeetCode contest")
    == "s'teL ekat edoCteeL tsetnoc"
)
assert sol.reverseWords("Mr Ding") == "rM gniD"
print("All test cases passed!")
