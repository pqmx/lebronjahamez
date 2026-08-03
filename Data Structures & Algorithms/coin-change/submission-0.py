class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = coins[::-1]
        needed = 0
        i = 0


        if needed == amount:
            return needed
        
        while amount > 0:
            if i >= len(coins):
                return -1
            if amount >= coins[i]:
                amount -= coins[i]
                needed += 1
            else:
                i += 1


        return needed



        