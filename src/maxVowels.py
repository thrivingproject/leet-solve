"""
Sliding Window — count vowels in the initial window of size k,
then slide by subtracting the outgoing char and adding the incoming char,
tracking the max count.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        the_vowels = set("aeiou")  # O(1)
        max_vowels = vowels = sum(1 for i in s[0:k] if i in the_vowels)  # O(k)

        for i in range(k, len(s)):  # O(n)
            if s[i - k] in the_vowels:
                vowels -= 1
            if s[i] in the_vowels:
                vowels += 1
            max_vowels = max(vowels, max_vowels)
        return max_vowels
