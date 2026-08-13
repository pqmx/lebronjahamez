class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        INF = 2 ** 31 - 1
        q = deque()
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        

        cur = 0
        while q:
            for _ in range(len(q)):
                r, c= q.popleft()
                for dr, dc in dir:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit and grid[nr][nc] != -1:
                        q.append([nr, nc])
                        visit.add((nr, nc))
                        grid[nr][nc] = cur + 1
            cur += 1

    
   
            


            



        


        