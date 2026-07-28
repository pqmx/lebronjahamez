import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subset(nums, [[]], 0)
    
    def subset(self, nums, sub, i):
        if i >= len(nums):
            return sub

        for j in range(len(sub)):
            arr = copy.deepcopy(sub[j])
            arr.append(nums[i])
            sub.append(arr)
        
        i += 1

        return self.subset(nums, sub, i)
        
        



        