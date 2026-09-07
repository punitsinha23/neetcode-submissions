class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m*n - 1
    
        while left <= right: 
            mid = (left + right)//2
            if target == matrix[mid//n][mid % n]:
                return True
            elif target > matrix[mid//n][mid % n]:
                left = mid + 1
            elif target < matrix[mid//n][mid % n]:
                right = mid - 1
        else:
            return False
        