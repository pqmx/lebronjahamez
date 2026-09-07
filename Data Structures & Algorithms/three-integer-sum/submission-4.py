class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        nums.sort()
        n = len(nums)


        for i in range(n):
            target = -nums[i]
            j = i + 1
            k = n -1
            while j < k:
                res = nums[i] + nums[j] + nums[k] # must equal 0
                if res > 0:
                    j -= 1
                elif res < 0:
                    i += 1
                else:
                    arr = [nums[i], nums[j], nums[k]]
