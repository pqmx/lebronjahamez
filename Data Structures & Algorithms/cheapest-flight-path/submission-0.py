class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        visited = set()
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

            if start in visited:
                continue

            if dst == start: # we have landed at our destination.
                res = min(res, curPrice)
                continue

            for price, end in adj[start]:
                
                heapq.heappush(h, [price + curPrice, end, curStops + 1])
            visited.add(start)



        if res == float("inf"):
            return -1
        return res



