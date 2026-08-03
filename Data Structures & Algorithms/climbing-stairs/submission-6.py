class Solution:
    def climbStairs(self, n: int) -> int:
        # basecase: number of steps is 0
        if n < 0:
            return 0
        if n < 3: #if number of steps is 1 or 2
            return n
        

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        