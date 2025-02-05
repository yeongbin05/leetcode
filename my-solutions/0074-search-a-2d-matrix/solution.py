class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        # top : 행렬 윗부분 row, bottom : 행렬 아랫부분 row
        top,bottom = 0,len(matrix) - 1
        row = - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            # 해당 행의 첫 원소와 마지막 원소 사이에 target이 있다면
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif target < matrix[mid][0]:
                bottom = mid - 1
            else:
                top = mid + 1
        if row == -1:
            return False
        left,right = 0,len(matrix[0])-1
        while right >= left:
            mid = (left + right) // 2
            if matrix[row][mid] > target:
                right = mid - 1
            elif matrix[row][mid] == target:
                return True
            else:
                left = mid + 1
        return False
