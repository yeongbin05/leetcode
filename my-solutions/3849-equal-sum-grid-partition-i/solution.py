class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n,m = len(grid),len(grid[0])
        # grid 안에 모든 값 합
        total = 0
        for i in range(n):
            for j in range(m):
                total += grid[i][j]
            
        row_sum,col_sum = [0]*n,[0]*m
        temp = 0
        for i in range(n):
            row_sum[i] = temp + sum(grid[i])
            temp = row_sum[i]
        
        temp = 0
        for col in range(m):
            col_sum[col] += temp
            for row in range(n):
                col_sum[col] += grid[row][col]
            temp = col_sum[col]

        for i in range(n):
            if row_sum[i] == total/2:
                return True

        for i in range(m):
            if col_sum[i] == total/2:
                return True

        return False
