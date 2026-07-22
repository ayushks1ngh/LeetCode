class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start, remain, path):
            if remain == 0:
                res.append(path[:])
                return
            if remain < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                dfs(i + 1, remain - candidates[i], path)
                path.pop()

        dfs(0, target, [])
        return res