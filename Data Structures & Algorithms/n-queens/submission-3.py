class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # lets do horsey way.
        diag = set()
        diag2 = set()
        col = set()
        board = [["."] * n for _ in range(n)]
        res = []

        def dfs(r):
            if r == n:
                copyBoard = ["".join(row[:]) for row in board]
                res.append(copyBoard)
                return
            for c in range(n):
                if r + c not in diag and r - c not in diag2 and c not in col:
                    board[r][c] = "Q" 
                    # add diagonals.
                    diag.add(r + c)
                    diag2.add(r - c)
                    col.add(c)

                    dfs(r + 1)

                    board[r][c] = "." 

                    diag.discard(r + c)
                    diag2.discard(r-c)
                    col.remove(c)



        dfs(0)
        return res