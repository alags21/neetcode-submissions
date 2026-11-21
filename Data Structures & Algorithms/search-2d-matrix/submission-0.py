class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        L,R = 0, rows * cols - 1
        while (L <= R):
            mid = (L + R) // 2
            r = mid // cols 
            c = mid % cols
            if (matrix[r][c] == target):
                return True
            elif (matrix[r][c] > target):
                R = mid - 1
            else:
                L = mid + 1
        
        return False