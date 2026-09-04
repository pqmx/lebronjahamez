class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
       

        most = text1 if len(text1) > len(text2) else text2
        mini = text2 if most == text1 else text1

        memo = [[None] * (len(mini) + 1) for _ in range(len(most))]


        def dfs(subI, totalI):
            if totalI >= len(most) or subI >= len(mini): 
                return 0

            if memo[totalI][subI] is not None:
                return memo[totalI][subI]
            

            if mini[subI] == most[totalI]:
                memo[totalI][subI] = 1 + dfs(subI + 1, totalI + 1)
            else:
                memo[totalI][subI] = max(dfs(subI, totalI + 1), dfs(subI + 1, totalI))


            return memo[totalI][subI]
    

        return dfs(0, 0)

            





