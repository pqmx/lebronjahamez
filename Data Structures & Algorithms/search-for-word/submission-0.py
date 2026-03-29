class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 1:
            for row in board:
                if word in row: return True
            return False

        def dfs(r, c, letter, visited):
            if letter == len(word):
                return True
            
            nRows, nCols = len(board), len(board[0])
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < nRows and 0 <= nc < nCols and (nr, nc) not in visited and board[nr][nc] == word[letter]:
                    visited.add((nr, nc))
                    if dfs(nr, nc, letter + 1, visited):
                        return True
                    visited.remove((nr, nc))
            return False

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 1, {(r, c)}):
                        return True
        return False