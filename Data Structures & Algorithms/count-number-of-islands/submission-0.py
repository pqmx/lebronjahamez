class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    sum += 1
                    self.dfs(grid, (i, j))
        return sum


    def dfs(self, grid, start):
        stack = [start]

        while stack:
            node = stack.pop()
            x, y = node

            grid[x][y] = "0"

            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                    stack.append((nx, ny))
                    grid[nx][ny] = "0"


    
        