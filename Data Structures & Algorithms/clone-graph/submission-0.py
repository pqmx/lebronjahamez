"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        

        
        def dfs(root, graph, visited = None):
            nonlocal head
            if graph is None:
                return


            #initiliaze our root.
            if root is None: # graph is not None
                root = Node(graph.val)
                head = root
            
            if not visited:
                visited = {}

            visited[root.val] = root
            
            # update root's neighbors (only val)
            for n in graph.neighbors:
                if n not in visited:
                    node = Node(n.val) # create new
                    root.neighbors.append(node) # append to root neighbors
                    visited[n] = node
                    dfs(node, n, visited) # update root's neighbors.
                else:
                    root.neighbors.append(visited[n])
                

        
        head = None
        dfs(None, node)
        return head
        

        

            
        