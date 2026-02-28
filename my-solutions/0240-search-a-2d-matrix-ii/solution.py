class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # n = 열 개수 , m = 행 개수
        n,m = len(matrix[0]),len(matrix)
        row,col = m-1 , 0
        
        while 0<=row<m and 0<=col<n:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True


        return False   
