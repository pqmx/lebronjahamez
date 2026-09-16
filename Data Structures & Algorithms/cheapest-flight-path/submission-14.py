class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #define relationships
        airports = {i : set() for i in range(n)}
        for start, end, price in flights:
            airports[start].add((price, end))
        
        res = float("inf")
        best_stops= {}
        # (cost, dst, stops)
        heap = [(0, src, -1)]
        while heap:
            cost, start, stops = heapq.heappop(heap)
            if start in best_stops:
                if stops < best_stops[start]:
                    best_stops[start] = stops
                else:
                    continue

            if start == dst:
                if stops <= k:
                    res = min(res, cost)
                    return res
                continue
            if stops >= k:
                continue

            for price, dest in airports[start]:
                heapq.heappush(heap, (cost + price, dest, stops + 1))
        


        if res == float("inf"):
            return -1
        return res






        
        