class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    self.dfs(board, (j, i))

    def dfs(self, board, start):

        stack = [start]
        altstack = [start]
        surrounded = True
        while stack:
            x, y = stack.pop()
            onEdge = (x == 0 or x == len(board[0]) - 1) or (y == 0 or y== len(board) - 1)
            if onEdge:
                surrounded = False
                
            dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            
            for dx, dy in dir:
                nx, ny = dx + x, dy + y
                if 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == "O":
                    stack.append((nx, ny))
                    altstack.append((nx, ny))
        
        if surrounded:
            while altstack:
               x, y = altstack.pop()
               board[y][x] = "X"

            
            


