
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        ans = 0
        minus_cnt = 0
        min_abs = float('inf')
        for col in range(n):
            for row in range(n):
                ans += abs(matrix[row][col])
                if abs(matrix[row][col]) < min_abs:
                    min_abs = abs(matrix[row][col])
                if matrix[row][col] < 0 :
                    minus_cnt += 1
        print(ans,min_abs,minus_cnt)
        if minus_cnt % 2 == 1:
            ans -= (2*min_abs)

        return ans
