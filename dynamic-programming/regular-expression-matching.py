class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0

        while i < len(s) and j < len(p):
            if p[j] == '.' or s[i] == p[j]:
                i += 1
                j += 1
            elif j + 1 < len(p) and p[j + 1] == '*':
                j += 2
            else:
                return False

        return i == len(s) and j == len(p)