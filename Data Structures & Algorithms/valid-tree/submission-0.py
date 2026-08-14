class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: # complete graphs has n -1 nodes
            return False

        visited = set()
        for src, dest in edges:
            if dest in visited:
                return False
            else:
                visited.add(dest)

        return True
