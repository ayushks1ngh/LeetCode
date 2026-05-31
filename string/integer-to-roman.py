class Solution:
    def intToRoman(self, num: int) -> str:

        values = [1000, 500, 100, 50, 10, 5, 1]
        symbols = ["M", "D", "C", "L", "X", "V", "I"]

        res = ""

        for i in range(len(values)):
            while num >= values[i]:
                res += symbols[i]
                num -= values[i]

        return res