class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = float("inf")
        cur = nums[0]
        while r < len(nums):
            if cur < target:
                r += 1
                if r >= len(nums):
                    break
                cur += nums[r]
            else:
                res = min(res,r - l)
                l += 1
                if l > r:
                    r += 1
                cur -= nums[l]
        
        
        if res == float("inf"):
            return 0
        return res
        


                


        