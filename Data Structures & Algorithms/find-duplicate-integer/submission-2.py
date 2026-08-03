class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = ""
        for n in nums:
            if str(n) + "*" in s:
                return n
            else:
                s += str(n) + "*"