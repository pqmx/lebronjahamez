class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    max_area = max(self.dfs(grid, (i, j)), max_area)
        return max_area

    def dfs(self, grid, start):
        stack = [start]
        path = 0
        while stack:
            coord = stack.pop()
            path += 1
            x, y = coord
            grid[x][y] = 0
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                nx, ny = dx + x, dy + y
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny]:
                    stack.append((nx, ny))
                    grid[nx][ny] = 0
        return path




                


                

                

