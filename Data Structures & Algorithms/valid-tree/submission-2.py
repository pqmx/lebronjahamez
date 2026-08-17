class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: # complete graphs has n -1 nodes
            return False

        rel = [[] for _ in range(n)]
        #visit all nodes.
    

        for src, dest in edges:
            rel[src].append(dest)
            rel[dest].append(src)
        
        visit = set()
        q = deque([(0, -1)])

        visit.add(0)

        while q:
            n, p = q.popleft()
            for ve in rel[n]:
                if n == p:
                    continue
                if n in visit:
                    return False
                visit.add(n)
                q.append((ve, n))

        return len(visited) == n




