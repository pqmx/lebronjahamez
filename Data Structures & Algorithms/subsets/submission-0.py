class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.subset(nums, [], 0)
    
    def subset(self, nums, sub, i):
        if i >= len(sub):
            return sub

        sub.append(nums[i])
        for j in range(i):
            arr = nums[j]
            arr.append(nums[i])
            sub.append(arr)
        
        i += 1

        return self.subset(nums, sub, i)
        
        



        