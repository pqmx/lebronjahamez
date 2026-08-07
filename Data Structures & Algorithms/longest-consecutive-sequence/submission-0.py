class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)
        res = 0

        for n in h:
            if n - 1 not in h:
                length = 1

                while n + length in h:
                    length += 1

                
                res = max(res, length)
        return res
        





        
            
        
        


                