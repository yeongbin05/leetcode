class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n,m = len(matrix),len(matrix[0])
        max_width = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '0':
                    max_width[i][j] = 0
                else:
                    max_width[i][j] = 1 if j == 0 else max_width[i][j-1] + 1
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if max_width[i][j] == 0:
                    continue
                row = i
                height = 1
                min_width = max_width[row][j]
                while row >= 0 and max_width[row][j] > 0 :         
                    min_width = min(min_width,max_width[row][j])
                    ans = max(ans,height * min_width)
                    height += 1
                    row -= 1
                

        return ans
