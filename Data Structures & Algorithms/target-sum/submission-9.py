class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = [None] * (n + 1)
        def dfs(i, cur):
            if i >= n:
                if cur == target:
                    return 1
                return 0
            

            if memo[i] is not None:
                return memo[i]
            curNum = nums[i]


            res = dfs(i + 1, cur + curNum) + dfs(i + 1, cur - curNum)
            return res
        

        return dfs(0, 0)
        
            




        