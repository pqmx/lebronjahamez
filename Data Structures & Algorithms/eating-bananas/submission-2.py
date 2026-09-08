class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            speed = (l + r) // 2

            hoursUsed = 0
            for p in piles:
                hoursUsed += math.ceil(p / speed)
            

            if hoursUsed <= h: # too fast.
                r = speed - 1
            elif hoursUsed > h:
                l = speed + 1

        return r

            


        
            



        

