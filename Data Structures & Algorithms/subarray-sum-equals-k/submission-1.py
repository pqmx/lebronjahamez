class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * n
        post = [0] * n

        for i in range(n):
            pre[i] = nums[i]
            if i != 0:
                pre[i] += pre[i - 1]


        for j in range(n - 1, -1, -1):
            post[j] = nums[j]
            if j != n - 1:
                post[j] += post[j + 1]


        res = 0
        for i in range(n):
            if post[i] == k:
                res += 1
            elif pre[i] == k:
                res += 1
            elif nums[i] == k:
                res += 1
        return res
    
            