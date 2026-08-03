class Solution:
    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[i][j] == "O":
                    self.dfs(board, (i, j))

    def dfs(self, board, start):

        stack = [start]

        while stack:
            x, y = stack.pop()
            dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            hasNeighbors = False
            for dx, dy in dir:
                nx, ny = dx + x, dy + y
                if 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[nx][ny] == "O":
                    hasNeighbors = True
                    stack.append((nx, ny))
                    board[nx][ny] = "X"
            
            if not hasNeighbors:
                return


