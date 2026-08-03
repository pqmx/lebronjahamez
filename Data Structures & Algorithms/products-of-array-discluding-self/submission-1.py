class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
        
        for i in range(len(nums)):
            nums[i] = prod / nums[i]
        return nums

        