class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[1])

        minHeap = []
        curCap = 0
        for curPass, start, end in trips:
            # check whether we are at a stop to drop off.
            while minHeap and minHeap[0][0] <= start:
                stop, passengerDrop = minHeap.pop()
                curCap -= passengerDrop
            # we add the passengers.
            curCap += curPass
            if curCap > capacity:
                return False
            heapq.heappush(minHeap, (end, curPass))
        

        return True
            

        

        