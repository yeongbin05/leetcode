class Solution(object):
    def islandPerimeter(self, grid):
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        
        # Define directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    for dx, dy in directions:
                        # Check boundary conditions
                        ni, nj = i + dx, j + dy
                        if ni < 0 or ni >= rows or nj < 0 or nj >= cols or grid[ni][nj] == 0:
                            perimeter += 1
        
        return perimeter
        
