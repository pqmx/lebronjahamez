class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.helper(nums, nums[1:], nums[:-1])

    
    def helper(self, nums, rob, robTwo):
        rob.append(0)
        robTwo.append(0)


        for i in range(len(nums) - 4, -1, -1):
            rob[i] += max(rob[i + 2], rob[i + 3])
            robTwo[i] += max(robTwo[i + 2], robTwo[i + 3])
        
        return max(rob[0], robTwo[0])




