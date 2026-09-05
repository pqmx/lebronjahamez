class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        def isConnected(graph, start, end):
            visited = set()
            stack = [start]
            while stack:
                node = stack.pop()
                if node == end:
                    return True
                visited.add(node)
                for v in graph[node]:
                    if v not in visited:
                        stack.append(v)


            return False


        graph = {i : set() for i in range(len(edges) + 1)}



        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            # we get the relationships
        



        for u, v in reversed(edges):
            graph[u].remove(v)
            graph[v].remove(u)
            if isConnected(graph, u, v):
                return [u, v]
            
            #add back the edge
            graph[v].add(u)
            graph[u].add(v)
            


