class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def dfs(path):

            if len(path) == 2 * n:
                result.append(path)
                return

            dfs(path + "(")
            dfs(path + ")")

        dfs("")

        return result