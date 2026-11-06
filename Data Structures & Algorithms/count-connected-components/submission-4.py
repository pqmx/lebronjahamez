class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        size = [1] * n
        count = n
        

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        def union(x, y):
            nonlocal count
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            if size[rx] > size[ry]:
                ry, rx = rx, ry
            parent[rx] = ry
            size[ry] += size[rx]
            count -=1
            return True


        for u, v in edges:
            union(u, v)
        return count