class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.targetSum(nums, target, 0, 0)
    
    def targetSum(self, nums, target, curVal, i):
        if i >= len(nums):
            return 0
        
        if curVal == target:
            return 1 + self.targetSum(nums, target, 0, i + 1)

        proj = curVal + nums[i]
        return self.targetSum(nums, target, proj if proj < target else curVal, i + 1)
