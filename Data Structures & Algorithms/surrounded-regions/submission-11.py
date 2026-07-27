class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (j, i) not in visited:
                    self.dfs(board, (j, i), visited)

    def dfs(self, board, start, visited):

        stack = [start]
        altstack = [start]
        visited.add(start)
        surrounded = True
        while stack:
            x, y = stack.pop()
            board[y][x] = "X"
            onEdge = (x == 0 or x == len(board[0]) - 1) or (y == 0 or y== len(board) - 1)
            if onEdge:
                surrounded = False
                
            dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for dx, dy in dir:
                nx, ny = dx + x, dy + y
                if 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == "O" and (nx, ny) not in visited:
                    stack.append((nx, ny))
                    altstack.append((nx, ny))
                    visited.add((nx, ny))
        
        if not surrounded:
            while altstack:
                x, y = altstack.pop()
                board[y][x] = "O"

            
            


