"""443"""


class Solution:
    def compress(self, chars: list[str]) -> int:
        last = ""
        count = 0
        write_p = 0
        for char in chars.copy():
            if last == char:
                count += 1
            else:
                if count > 1:
                    digits = [d for d in str(count)]
                    for d in digits:
                        chars[write_p] = d
                        write_p += 1
                chars[write_p] = char
                write_p += 1
                count = 1
                last = char

        if count > 1:
            digits = [d for d in str(count)]
            for d in digits:
                chars[write_p] = d
                write_p += 1

        return write_p
