class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        dist = {}
        min_d = float('inf')
        for p in points:
            distance = math.sqrt(p[0] ** 2 + p[1] ** 2)
            if distance in dist:
                dist[distance].append(p)
            else:
                dist[distance] = [p]
            
            min_d = min(min_d, distance)
        
        return dist[min_d]

        

        