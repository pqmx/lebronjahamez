class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numdict = {num:i for i, num in enumerate(nums)}
        for n in nums:
            val = target - n
            if val in numdict and numdict[n] != numdict[val]:
                return [numdict[n], numdict[val]]