class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMin = 1
        curMax = 1

        for n in nums:
            if n == 0:
                curMin = 1
                curMax = 1
            else:
                a = curMin * n
                b = curMax * n
                curMin = min(curMin, a, b)
                curMax = max(curMax, a, b)
            res = max(res, curMax)
        
        return curMax