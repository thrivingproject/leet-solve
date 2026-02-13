# count consecutive digits
# once it changes, count again
# once it changes, return smaller of first count and second count
# go back to where first count ended/second count started
# repeat
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        total_count = 0

        i = 0
        while i < len(s):
            start = i
            count_1 = 1
            while i < len(s) - 1 and s[i + 1] == s[i]:
                i += 1
                count_1 += 1
            if i == len(s) - 1:
                break
            count_2 = 1
            i += 1
            while i < len(s) - 1 and s[i + 1] == s[i]:
                i += 1
                count_2 += 1
            smaller = min(count_1, count_2)
            total_count += smaller
            i = start + count_1
        return total_count
