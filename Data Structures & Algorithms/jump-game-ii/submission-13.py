class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        jumps = 0
        while i < len(nums)- 1:
            options = nums[i]
            jumps += 1
            if i + options >= len(nums) - 1:
                return jumps

            i += 1
            k = i
            for j in range(i, i + options):
                if nums[j] + j >= nums[k] + k:
                    k = j
            i = k
        return 0


            
            

                


            

        