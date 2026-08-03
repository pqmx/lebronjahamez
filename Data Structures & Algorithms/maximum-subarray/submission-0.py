class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0


        sum = arr[0]
        max_sum = arr[0]

        for n in nums[1::]:
            sum = max(sum, n)
            max_sum = max(sum, max_sum)
        return max_sum