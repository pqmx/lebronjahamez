class MedianFinder:
    def __init__(self):
        self.lo  = [] # use negative.
        self.hi= []




    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        if len(self.lo) - len(self.hi) >= 2: # if imbalanced we must rebalance.
            temp = -heapq.heappop(self.lo)
            heapq.heappush(self.hi, temp)



        if self.lo and self.hi and -self.lo[0] > self.hi[0]:
            lotemp = -heapq.heappop(self.lo)
            hitemp = heapq.heappop(self.hi)
            heapq.heappush(self.hi, lotemp)
            heapq.heappush(self.lo, -hitemp)



            


        



        

        



    def findMedian(self) -> float:
        if (len(self.lo) + len(self.hi)) % 2 == 0:
           return (-self.lo[0] + self.hi[0]) / 2
        else:
            if len(self.hi) > len(self.lo):
                return self.hi[0]
            else:
                return -self.lo[0]
        
        




