class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        pacific = []
        atlantic = []

        for i in range(len(pac[0])):
            pacific.append((0, i))
            atlantic.append((len(atl) - 1, i))
        for i in range(len(pac)):
            pacific.append((i, 0))
            atlantic.append((i, len(atl[0]) - 1))

        self.bfs(heights, pacific, pac)
        self.bfs(heights, atlantic, atl)


        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append((r, c))
        return res

    def bfs(self, heights, start, ocean):
        ROWS, COLS = len(heights), len(heights[0])
        q = deque(start)
        visited = set()
        while q:
            r, c = q.pop()
            ocean[r][c] = True
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = dr + r, dc + c

                if (nr, nc) not in visited and 0 <= nr < ROWS and 0 <= nc < COLS and heights[r][c] <= heights[nr][nc]:
                    q.append((nr, nc))
                    visited.add((nr, nc))
        
        
                
                


                

        