class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i,canBuy):
            if (i,canBuy) in memo:
                return memo[(i,canBuy)]

            if i >= len(prices):
                # res = max(cur, res)
                return 0

                
            total = 0
            if canBuy:
                buy = dfs(i + 1, False) - prices[i] # we buy, subtract from our profit. lose buying power.
                skip = dfs(i + 1,True) # we skip nothing happens
                total = max(buy, skip)
            else:
                # we need to sell or skip selling
                sell = dfs(i + 2, True) + prices[i] # buying power granted + skips next day for us.
                skip = dfs(i + 1,False) # nothing changes.
                total = max(sell, skip)
            
            memo[(i,canBuy)] = total
            return memo[(i,canBuy)]

        return dfs(0, True)

        



        