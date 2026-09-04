class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}
        words = set(wordDict)



        def dfs(i):
            if i == n:
                return True
            if i in memo:
                return memo[i]
            # we haven't done it yet

            for j in range(i + 1, n + 1):
                if s[i: j] in words and dfs(j):
                    memo[i] = True
                    return memo[i]

            memo[i] = False
            return False

        return dfs(0)




        