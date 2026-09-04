class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = [[None] * (amount + 1) for _ in range(len(coins) + 1)]
        
        def dfs(i, target):


            if target == 0:
                return 1

            if i >= len(coins):
                return 0
            


            if memo[i][target] is not None:
                return memo[i][target]


            if coins[i] <= target:
                
                exclude = dfs(i + 1, target)
                include = dfs(i, target - coins[i])

                memo[i][target] = exclude + include
                return memo[i][target]

            else:

                memo[i][target] = dfs(i + 1, target)
                return memo[i][target]
        
        return dfs(0, amount)