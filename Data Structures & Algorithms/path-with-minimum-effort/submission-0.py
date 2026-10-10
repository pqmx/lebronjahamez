class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        eR, eC = len(heights) - 1, len(heights[0]) - 1
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        h = [(0, 0, 0)]

        dist = [ [float("inf")] * len(heights[0]) for height in heights]


        # djikstra's algorithm
        # find min |x - y| among two numbers in each path from 0, 0 to l-1,l-1


        # we can't have visited since we can't assume that it is invalid, once we visit it we could reach that path from another new height, we must compute absoulte minimum cost. and keep that among.
        while h:
            e, r, c = heapq.heappop(h)

            # we reached end.
            if r == eR and c == eR:
                return e
            
            # 
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr <= eR and 0 <= nc <= eC:
                    MAD = abs(heights[r][c] - heights[nr][nc])
                    minEffort = max(e, MAD)
                    if minEffort < dist[nr][nc]:
                        dist[nr][nc] = minEffort
                    else:
                        continue
                    heapq.heappush(h, (minEffort, nr, nc))


        


        