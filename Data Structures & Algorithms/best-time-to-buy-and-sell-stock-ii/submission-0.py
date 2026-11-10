class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = [[None, None] for _ in range(n)]


        def dp(i, holding):

            if i == n:
                return 0
            
            if profit[i][holding] is not None:
                return profit[i][holding]
            


            skip = dp(i + 1, holding)
            if holding:
                act = prices[i] + dp(i + 1, False)
            else:
                act = -prices[i] + dp(i + 1, True)
            profit[i][holding] = max(act, skip)
            return profit[i][holding]

        


        return dp(0, False)