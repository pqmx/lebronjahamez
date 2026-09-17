class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # n = len(nums)
        # dp = [0 * (n + 1)]

        # for i in range(n+1):
        dp = {}
        def dfs(target):
            if target in dp:
                return dp[target]
            if target == 0:
                return 1
            
            if target < 0:
                return 0
            

            ways = 0
            for n in nums:
                
                ways += dfs(target - n)
            
            dp[target] = ways
            return dp[target]

        
        return dfs(target)