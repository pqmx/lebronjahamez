class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r =0, 0
        window, target = {}, {}
        
        for c in t:
            if c not in target:
                target[c] = 1
            else:
                target[c] += 1

        def isMatch(window, target):
            for c in target:
                if c not in window or window[c] < target[c]:
                    return False
            return True

        have, need = 0, len(target)
        l, r = 0, 0
        res, windowLength = "", float("inf")

        while r < len(s):
            # find recurrence
            while have < need and r < len(s):
                c = s[r]
                window[c] = window.get(c, 0) + 1
                if c in target and window.get(c, 0) == target[c]:
                    have += 1
                r += 1
            
            # optimization
            while have == need:
                if r - l < windowLength:
                    windowLength = r-l
                    res = s[l : r]
                c = s[l]
                window[c] -= 1
                
                if c in target and window[c] < target[c]:
                    have -= 1
                l += 1
        return res


            
            






                




