class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()

        def dfs(i, arr, goal):
            if goal == 0:
                res.append(arr.copy())
                return
            
            if i >= n or candidates[i] > goal:
                return 

            arr.append(candidates[i])
            dfs(i + 1, arr, goal - candidates[i])
            arr.pop()


            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, arr, goal)


        dfs(0, [], target)
        return res