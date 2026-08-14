class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [True] * n
        dp[0] = ["()"] # represents 1 pair.


        for i in range(1, n):
            dp[i] = []
            for p in dp[i - 1]:
                if p + "()" != "()" + p:
                    dp[i].append(p + "()")
                dp[i].append("()" + p)
                dp[i].append("(" + p + ")")
                

                
            
        return dp[-1]