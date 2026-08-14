class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n+1)]
        dp[0].append("") # represents 1 pair.


        for pairs in range(1, n+1):
            for inside in range(pairs):
                outside = pairs - 1 - inside



                for A in dp[inside]:
                    for B in dp[outside]:
                        dp[pairs].append("(" + A + ")" + B)
                
        
        return dp[-1]

            


                

                
            
        return list(dp[-1])