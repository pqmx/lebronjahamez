class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: # complete graphs has n -1 nodes
            return False

        visited = set()
        for src, dest in edges:
            if dest in visited:
                return False
            else:
                if src > dest:
                    visited.add((dest, src))
                else:
                    visited.add((src, dest))

        return True
