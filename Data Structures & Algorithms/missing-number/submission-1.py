class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        setNums = set(nums)
        for i in range(len(setNums)):
            if i not in setNums:
                return i
        
        return i + 1
        