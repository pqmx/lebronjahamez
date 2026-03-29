class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {num:i for i, num in enumerate(nums)}
        for i, n in enumerate(nums):
            val = target - n
            if val in numdict and i != numdict[val]:
                return [i, numdict[val]]