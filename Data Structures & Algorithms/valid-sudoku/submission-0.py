class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            
            if len(board[i]) != len(set(board[i])):
                return False
            
            
            col = []
            for j in range(9):
                col.append(board[i][j])


                if i % 3 == 0 and j % 3 == 0:
                    square = []
                    for y in range(i, i + 3):
                        for x in range(j, j +3):
                            square.append(board[y][x])
                
                    if len(square) != len(set(square)):
                        return False


            if len(col) != len(set(col)):
                return False

        return True




            

                
        