class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1
        
        for n in nums:
            if m[n] == 1:
                return n
        