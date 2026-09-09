class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, cur, canBuy):
            if (i, cur) in memo:
                return memo[(i, cur)]

            if i >= len(prices):
                # res = max(cur, res)
                memo[(i, cur)] = cur
                return memo[(i, cur)]
            total = 0
            if canBuy:
                buy = dfs(i + 1, cur - prices[i], False) # we buy, subtract from our profit. lose buying power.
                skip = dfs(i + 1, cur, True) # we skip nothing happens
                total = max(buy, skip)
            else:
                # we need to sell or skip selling
                sell = dfs(i + 2, cur + prices[i], True) # buying power granted + skips next day for us.
                skip = dfs(i + 1, cur, False) # nothing changes.
                total = max(sell, skip)
            
            memo[(i, cur)] = total
            return memo[(i, cur)]

        return dfs(0, 0, True)

        



        