class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        res = float("inf")
        for start, end, price in flights:
            if start not in adj:
                adj[start] = []
            adj[start].append([price, end])



        #design fo heap price, start, stops
        h = [[0, src, -1]]
        while h:
            curPrice, start, curStops = heapq.heappop(h)

            if curStops > k:
                continue

            if dst == start: # we have landed at our destination.
                res = min(res, curPrice)
                continue

            if start not in adj:
                continue
            

            for price, end in adj[start]:
                    heapq.heappush(h, [price + curPrice, end, curStops + 1])



        if res == float("inf"):
            return -1
        return res



