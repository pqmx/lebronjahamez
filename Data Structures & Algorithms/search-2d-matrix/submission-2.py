class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        stack = []
        for i in range(len(matrix)):
            if target > matrix[i][0]:
                stack = matrix[i]
            if target < matrix[i][0]:
                break;
            if target == matrix[i][0]:
                return True

        if not stack:
            return False
        chosen = stack.pop()

        for n in chosen:
            if n == target:
                return True

        return False