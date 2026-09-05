class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def dfs(i, cur):
            if i >= n:
                if cur == target:
                    return 1
                return 0
            

            curNum = nums[i]
            add = cur + curNum
            sub = cur - curNum


            if (i, sub) in memo and (i, add) in memo:
                return memo[(i, add)] + memo[(i, sub)]

            

            res = 0
            if (i, add) not in memo:
                memo[(i, add)] = dfs(i + 1, add)
            res += memo[(i, add)]
            if (i, sub) not in memo:
                 memo[(i, sub)] = dfs(i + 1, sub)
            res += memo[(i, sub)]

            return res
        

        return dfs(0, 0)
        
            




        