class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        og = len(nums)
        for i in range(og * 2):
            if i < len(nums):
                ans.append(nums[i])
            else:
                ans.append(nums[i - og])
        
        return ans
        