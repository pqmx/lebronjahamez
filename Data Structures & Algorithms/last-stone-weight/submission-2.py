class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:  
        max_heap = []
        for s in stones:
            heapq.heappush(max_heap, -s)

        while len(max_heap) > 1:
            max = -heapq.heappop(max_heap)
            max2 = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, max2 - max)
        
        return -max_heap[0]


            




        