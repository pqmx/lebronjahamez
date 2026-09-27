class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        # the minimum capacity must be max(weights)
        #
        dayAttempted = 0
        while l <= r:
            cap = (l + r) // 2
            cur = 0
            dayAttempted = 0
            i = 0
            while i < len(weights):
                if cur + weights[i] < cap:
                    cur += weights[i]
                    i += 1
                elif cur + weights[i] > cap:
                    cur = 0
                    dayAttempted += 1
                else:
                    cur = 0
                    dayAttempted += 1
                    i += 1
            if cur:
                dayAttempted += 1

            if dayAttempted <= days:
                r -= 1
            else:
                l += 1
        
        return l

        