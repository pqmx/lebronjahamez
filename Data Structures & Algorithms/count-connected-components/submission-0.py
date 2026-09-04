class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        graph = {i : set() for i in range(n)}
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        

        def dfs(i, visited):
            if i in visited:
                return False
            
            visited.add(i)
            for a in graph[i]:
               dfs(a, visited)
    
            return True
        

        res = 0
        visited = set()
        for j in range(n):
            if dfs(j, visited):
                res += 1
        return res
            
        

