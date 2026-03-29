class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        profit = 0
        for i, p in enumerate(prices):
            # if we hit a new min
            if p < prices[buy]:
                buy = i
                if len(prices) - 1 != i:
                    sell = i + 1
                else:
                    return profit
            # we hit a new max
            if p - prices[buy] > profit:
                profit = p - prices[buy]
                sell = i


        return profit