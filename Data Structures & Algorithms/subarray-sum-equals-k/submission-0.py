class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * n

        for i in range(n):
            pre[i] = nums[i]
            if i != 0:
                pre[i] += nums[i - 1]

        res = 0
        for j in pre:
            if j == k or j - k:
                res += 1
        return res
            