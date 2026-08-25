import heapq

class Solution:
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1, n + 1):
            adj[i] = []
        

        for src, dest, weight in times:
            adj[src].append([dest, weight])
        
        visited = {}
        heap = [[0, k]]
        while heap:
            weight, src = heapq.heappop(heap)

            if src in visited:
                continue

            visited[src] = weight
        
            for dest, weight2 in adj[src]:
                heapq.heappush(heap, [weight + weight2, dest])
        


        if len(visited) == n:
            return max(visited.values())
        else:
            return -1
        


            


        
        

        








        


        