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
                a = curMax * n
                curMin = min(curMax * n, n * curMin, n)
                curMax = max(a, n * curMin, n)
                res = max(res, curMax)
        
        return res