class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [set() for _ in range(n)]
        dp[0].add("()") # represents 1 pair.


        for i in range(1, n):
            dup = set()
            for p in dp[i - 1]:
                dp[i].add(p + "()")
                dp[i].add("()" + p)
                dp[i].add("(" + p + ")")


                

                
            
        return list(dp[-1])