class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        memoArr = [None] * (n + 1)
        def dfs(i, cur):
            if i >= n:
                if cur == target:
                    return 1
                return 0
            

            if memoArr[i] is not None:
                return memoArr[i]
                
            curNum = nums[i]

            memo[(i, cur + curNum)] = dfs(i + 1, cur + curNum)
            memo[(i, cur - curNum)] = dfs(i + 1, cur - curNum)
            return memo[(i, cur + curNum)] +  memo[(i, cur - curNum)]
        

        return dfs(0, 0)
        
            




        