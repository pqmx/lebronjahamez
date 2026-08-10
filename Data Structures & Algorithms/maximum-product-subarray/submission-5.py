class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        # start at the second element.
        lastNegative = False # last number was negative?
        for i in range(len(nums) - 2, -1, -1):
            prev = nums[i + 1]
            if lastNegative and prev > 0:
                prev *= -1
            lastNegative = nums[i] < 0 
            
            nums[i] = max(nums[i], nums[i] * prev)
            res = max(res, nums[i])


        
        return max(nums[0], res)