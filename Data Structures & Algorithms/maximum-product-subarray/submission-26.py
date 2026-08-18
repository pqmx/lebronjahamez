class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        curMax = 1
        curMin = 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            temp = curMin * n
            curMax = max(curMax * n, curMin * n, n)
            curMin = max(temp, curMin * n, n)
            res = max(res, curMax)
        return res
            