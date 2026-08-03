class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = nums[0]
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] < min:
                min = nums[l]
            if nums[r] < min:
                min = nums[r]
            l += 1
            r -= 1
        return min
            