class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if j == len(p):
                return i == len(s)

            first = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )

            if first:
                ans = dfs(i + 1, j + 1)
            else:
                ans = False

            memo[(i, j)] = ans
            return ans

        return dfs(0, 0)