class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, = 0, len(nums) - 1
        m = r // 2


        while l <= r:

            if nums[m] == target or nums[l] == target or nums[r] == target:
                return m

            if nums[m] < target:
                l = m
            if nums[m] > target:
                r = m
            m = (l + r) // 2
            



        