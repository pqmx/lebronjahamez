class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        return self.climbStair(n, memo)
    def climbStair(self, n: int, memo: Dict[int, int]):
        # basecase: number of steps is 0
        if n < 3: #if number of steps is 1 or 2
            memo[n] = n
            return n
        if n not in memo:
            memo[n] = self.climbStair(n - 1, memo) + self.climbStair(n - 2, memo)

        return memo[n] 