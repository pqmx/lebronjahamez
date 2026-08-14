class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n == ".": 
                    continue

                if n in rows[i]:
                    return False
                else:
                    rows[i].add(n)
                
                if n in cols[j]:
                    return False
                else:
                    cols[j].add(n)


                # 4 // 2 = 2
                #
                rowStart = (i // 3) * 3
                colStart = j // 3
                c = rowStart + colStart
                if n in squares[c]:
                    return False
                else:
                    squares[c].add(n)
        return True
                
