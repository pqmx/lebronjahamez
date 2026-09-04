class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        
        memo = [[None] * (target + 1) for _ in range(len(nums))]


        def searchTarget(i, currentSum):
            if currentSum == target:
                return True
            elif currentSum > target or i >= len(nums):
                return False
            if memo[i][currentSum] is not None:
                return memo[i][currentSum]
            

            # we can choose to add or not add.
            include = searchTarget(i + 1, currentSum + nums[i])
            exclude = searchTarget(i + 1, currentSum)
            

            memo[i][currentSum] = include or exclude

            return memo[i][currentSum]
                
        
        return searchTarget(0, 0)
            

            
