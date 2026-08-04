class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        infected = deque()
        fresh = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                if grid[i][j] == 2:
                    infected.append((i, j))
                
        

       

        if not fresh:
            return 0

        minute = -1
        while infected: #still in 
            for _ in range(len(infected)): # we get len of infected at that time first -> dont get too deep.
                self.bfs(grid, infected, fresh)
            minute += 1
        

        #remaining fresh fruits
        return -1 if fresh else minute
    
    def bfs(self, grid, infected, fresh):
        dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        r, c = infected.popleft()
        for nr, nc in dir:
            #unvisited.
            tr, tc= r + nr, c + nc
            if 0 <= tr < len(grid) and 0 <= tc < len(grid[0]) and grid[tr][tc] == 1:
                grid[tr][tc] = 2 #mark as visited.
                fresh.discard((tr, tc)) 
                infected.append((tr, tc)) 


                


        