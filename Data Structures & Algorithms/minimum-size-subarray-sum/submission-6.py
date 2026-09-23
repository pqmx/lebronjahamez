class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = float("inf")
        cur = 0
        while r < len(nums):
            if cur < target and l != r:
                r += 1
                if r >= len(nums):
                    break
                cur += nums[r]
            else:
                res = min(res,r - l)
                cur -= nums[l]
                l += 1

        
        
        if res == float("inf"):
            return 0
        return res
        


                


        