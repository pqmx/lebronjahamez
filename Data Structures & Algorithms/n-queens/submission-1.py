class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        right = [(1, 2), (2, -1)] # shallowright -> hard left
        left = [(1, -2), (2, 1)] # shallow left -> hard right

        res = []

        def isValid(r, c):
            return 0 <= r < n and 0 <= c < n

        def dfs(pos, isRight, board, queensPlaced):
            r, c = pos
            directions = left
            if isRight:
                directions = right
            
            lastVisited = None

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if isValid(nr, nc):
                    queensPlaced += 1
                    lastVisited = (nr, nc)
                    board[nr][nc] = 'Q'

            if lastVisited is None: # we ran out of places.
                if queensPlaced == n:
                    return True
                return False

            return dfs((nr, nc), isRight, board, queensPlaced)
        

        for i in range(n):
            temp1 = [r[:] for r in board]
            temp1[0][i] = 'Q'
            if dfs((0, i), True, temp1, 1) and len(res) < n:
                temp1 = ["".join(b) for b in temp1]
                res.append(temp1)
            temp2 = [r[:] for r in board]
            temp2[0][i] = 'Q'
            if dfs((0, i), False, temp2, 1) and len(res) < n:
                temp2= ["".join(b) for b in temp2]
                res.append(temp2)
        
        
        return res
        