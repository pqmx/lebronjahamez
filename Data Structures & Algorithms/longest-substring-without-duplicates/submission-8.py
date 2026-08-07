class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_val = 0
        chars = set()
        l = 0
        r = 0

        cur = 0



        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                cur += 1
                r += 1
            else:
                max_val = max(max_val, cur)
                chars = set()
                cur = 0
                l = r
        max_val = max(max_val, cur)
        
        return max_val
            
            
        

