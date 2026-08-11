class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            # do we reach the raw endpoint

            # if not lets investigate the current number it is pointing too
            anyTrue = False
            for j in range(i + 1, i + nums[i] + 1):
                if dp[j]:
                    anyTrue = True
                    break

            if anyTrue:
                dp[i] = True
        

        return dp[0]
    
            
            
        
            


            
            
            


