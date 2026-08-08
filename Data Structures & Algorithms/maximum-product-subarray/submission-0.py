class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        # start at the second element.
        for i in range(len(nums) - 2, -1, -1):
            nums[i] = max(nums[i], nums[i] * nums[i + 1])
            res = max(res, nums[i])
        
        return res