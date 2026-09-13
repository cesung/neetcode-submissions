class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m * n
        m, n = len(matrix), len(matrix[0])
        # find the first element at the last column with value >= to target
        left, right = 0, m - 1
        while left < right:
            mid = (left + right) // 2
            if matrix[mid][-1] < target:
                left = mid + 1
            else:
                right = mid
        
        if matrix[left][-1] < target:
            return False
        
        row = left
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if matrix[row][mid] > target:
                right = mid - 1
            else:
                left = mid
        
        if matrix[row][left] != target:
            return False
        
        return True
