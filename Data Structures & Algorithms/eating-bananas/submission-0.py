class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1
        while True:
            hoursUsed = 0
            for p in piles:
               hoursUsed += math.ceil(p/speed)
               
            if hoursUsed <= h:
                return speed
            

            speed += 1
            



        

