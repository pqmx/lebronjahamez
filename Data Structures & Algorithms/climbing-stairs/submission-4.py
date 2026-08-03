class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n < 3:
            return n
        

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        