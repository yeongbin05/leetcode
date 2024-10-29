class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # ans = 0
        # m = len(grid)
        # n = len(grid[0])
        
        # dp = [[0]*n for _ in range(m)]
        # def dfs(i,j,temp):
        #     flag = False
            
        #     if i == m or j == n:
        #         return temp
        #     if 0<=i-1<m and 0<=j+1<n and grid[i-1][j+1] > grid[i][j]  :
        #         dp[i-1][j+1] = max(dp[i-1][j+1],dp[i][j] + 1)
        #         if max(dp[i-1][j+1],dp[i][j] + 1) > temp :
        #             temp = max(dp[i-1][j+1],dp[i][j] + 1)
        #         dfs(i-1,j+1,temp)
        #         flag = True
                    
                

        #     if 0<=i<m and 0<=j+1<n and grid[i][j+1] > grid[i][j]  :
                
        #         dp[i][j+1] = max(dp[i][j+1],dp[i][j] + 1)
        #         if max(dp[i][j+1],dp[i][j] + 1) > temp:
        #             temp = max(dp[i][j+1],dp[i][j] + 1)
        #         dfs(i,j+1,temp)
        #         flag = True
                
        #     if 0<=i+1<m and 0<=j+1<n and grid[i+1][j+1] > grid[i][j]  :
        #         dp[i+1][j+1] = max(dp[i+1][j+1],dp[i][j] + 1)
        #         if max(dp[i-1][j+1],dp[i][j] + 1) > temp:
        #             temp = max(dp[i-1][j+1],dp[i][j] + 1)
        #         dfs(i+1,j+1,temp)
        #         flag = True
            
        #     if flag == False:
        #         return temp
        # for row in range(m):
        #     temp = 0 
        #     dp = [[0]*n for _ in range(m)]
        #     res = dfs(row,0,temp)           
        #     for d in dp :
        #         # print(d)
        #         if max(d) > ans:
        #             ans = max(d)
                    
        
        

      
        # return ans
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            
            max_move = 0
            for ni, nj in [(i-1, j+1), (i, j+1), (i+1, j+1)]:
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    max_move = max(max_move, 1 + dfs(ni, nj))
            
            dp[i][j] = max_move
            return dp[i][j]

        ans = 0
        for row in range(m):
            ans = max(ans, dfs(row, 0))
        
        return ans
