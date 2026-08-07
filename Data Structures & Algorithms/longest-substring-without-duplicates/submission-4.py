class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_val = 0

        # if not s:
        #     return max_val

        

        letters = set()
        l = 0
        r = 0

        cur = 0
        while r < len(s):
            if s[r] not in letters:
                letters.add(s[r])
                cur += 1
                r += 1
            else:
                max_val = max(max_val, cur)
                letters = set()
                cur = 0
                l = r
        
        return max_val
            
            
        

