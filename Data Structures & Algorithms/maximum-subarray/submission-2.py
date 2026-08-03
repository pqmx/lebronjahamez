class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0


        isum = nums[0]
        max_sum = nums[0]

        for n in nums[1::]:
            isum = max(isum, n)
            max_sum = max(isum, max_sum)
        return max_sum