class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        for n in nums:
            product *= n


        for i in range(len(nums)):
            nums[i] = product ^ nums[i]
        
        return nums