class Solution:
    def reverseByType(self, s: str) -> str:
        alphas = []
        symbols = []
        new_s = ""
        for char in s:
            if char.isalpha():
                alphas.append(char)
            else:
                symbols.append(char)
        for char in s:
            if char.isalpha():
                new_s += alphas.pop()
            else:
                new_s += symbols.pop()
        return new_s
