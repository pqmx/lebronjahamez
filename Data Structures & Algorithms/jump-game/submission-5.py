class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [True] * len(nums)

        for i in range(len(nums)):

            if nums[i] == 0 or not dp[i]:
                dp[i] = False
                continue

            for j in range(i + 1, nums[i]):
                if j > len(nums):
                    break;

                if nums[j] == 0 or not dp[j]:
                    dp[j] = False
                    continue 
        return not dp[-1]
            
            


