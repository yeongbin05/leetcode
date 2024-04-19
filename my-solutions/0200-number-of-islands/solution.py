class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
    
        rows, cols = len(grid), len(grid[0])
        
        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == '0':
                return
            grid[row][col] = '0'  # Marking the cell as visited
            
            # Recursively call DFS on adjacent cells
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
                    
        return count
            
