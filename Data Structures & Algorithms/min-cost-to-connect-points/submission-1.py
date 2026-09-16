class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        heap = [(0, 0)]
        res = 0



        while len(visited) < n:
            cost, p = heapq.heappop(heap)
            if p in visited:
                continue
            xi, yi = points[p]

            for j in range(n):
                if j in visited or j == p:
                    continue
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                heapq.heappush(heap, (dist, j))

            res += cost
            visited.add(p)
        

        return res




        
