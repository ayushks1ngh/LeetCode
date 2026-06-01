class Solution:
    def isValid(self, s: str) -> bool:

        opens = 0
        closes = 0

        for ch in s:
            if ch in "([{":
                opens += 1
            else:
                closes += 1

        return opens == closes