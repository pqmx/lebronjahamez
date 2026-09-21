class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        
        for n in nums:
            if n == 1:
                cur += 1
                res = max(res, cur)
            else:
                
                cur = 0
        
        return res
        