class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0

        mp = {}
        res = 0
        maxFreq = 0
        replace = 0

        while l <= r and r < len(s):
            if s[r] not in mp:
                mp[s[r]] = 1
            else:
                mp[s[r]] += 1

            maxFreq = max(maxFreq, max(mp.values()))

            #when can we not move right? when there is more than k 
            # different characters we need to replace.


            replace = sum(mp.values()) - maxFreq
            if replace > k:
                # get length from l to r - 1
                res = max(res, r- l)

                mp[s[l]] -= 1
                l += 1
            r += 1
        res = max(res, r - l)
        

        return res

