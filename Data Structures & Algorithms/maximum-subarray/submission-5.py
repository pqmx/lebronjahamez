class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev = nums[0]
        total = nums[0]


        for i in range(1, len(nums), 1):
            prev = max(nums[i], nums[i] + prev)
            total = max(total, prev)
        total = max(total, prev)
    
        return total




        