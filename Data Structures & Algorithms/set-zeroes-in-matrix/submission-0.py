class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        firstColumnZero = False
        firstRowZero = False
        

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    if r == 0:
                        firstRowZero = True
                    if c == 0:
                        firstColumnZero = True
                    

                    matrix[0][c] = True
                    matrix[r][0] = True
        

        for r in range(1, len(matrix)):
            if matrix[r][0] == True:
                matrix[r] = [0] * len(matrix[r])
        
        for c in range(1, len(matrix)):
            if matrix[0][c] == True:
                for n in range(len(matrix)):
                    matrix[n][c] = 0
        
        if firstRowZero:
            matrix[0] = [0] * len(matrix[0])

        if firstColumnZero:
            for n in range(len(matrix)):
                matrix[n][0] = 0


    
        
    
        


        