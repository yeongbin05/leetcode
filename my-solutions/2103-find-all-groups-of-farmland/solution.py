class Solution(object):
    def findFarmland(self, land):
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or land[r][c] == 0:
                return [r-1, c-1]
            
            land[r][c] = 0
            bottomRight = dfs(r+1, c)
            rightBottom = dfs(r, c+1)
            
            bottomRight = [max(bottomRight[0], r), max(bottomRight[1], c)]
            rightBottom = [max(rightBottom[0], r), max(rightBottom[1], c)]
            
            return [max(bottomRight[0], rightBottom[0]), max(bottomRight[1], rightBottom[1])]
        
        m, n = len(land), len(land[0])
        farmlands = []
        
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    topLeft = [i, j]
                    bottomRight = dfs(i, j)
                    farmlands.append(topLeft + bottomRight)
        
        return farmlands
