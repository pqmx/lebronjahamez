class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r =0, 0
        window = {}
        target = {}
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

        

        # find first recurrence
        # shrink the window (left pointer) as much as possible
        # once it is not keep expanding with right to see if we find a new
        
        l, r = 0, 0
        res = ""
        windowLength = float("inf")
        while r < len(s):
            # find recurrence
            while not isMatch(window, target) and r < len(s):
                c = s[r]
                window[c] = window.get(c, 0) + 1
                r += 1
            
            # optimization
            while isMatch(window, target):
                if r - l < windowLength:
                    windowLength = r-l
                    res = s[l : r]
                c = s[l]
                window[c] -= 1
                if window[c] <= 0:
                    del window[c]
                l += 1
        return res


            
            






                




