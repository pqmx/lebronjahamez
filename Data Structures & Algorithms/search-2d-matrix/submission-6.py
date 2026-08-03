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
    
        l, r = 0
        len(stack) - 1
        while l <= r:
            mid = (left + right) // 2
            if stack[mid] < target:
                left = mid + 1
            elif stack[mid] > target:
                right = mid + 1
            else:
                return True




        return False