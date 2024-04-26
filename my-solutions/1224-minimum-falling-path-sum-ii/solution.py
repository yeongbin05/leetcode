class Solution(object):
    def minFallingPathSum(self, grid):
        n = len(grid)
    
        # Iterate through each row starting from the second row
        for i in range(1, n):
            # Iterate through each column
            for j in range(n):
                # Initialize the minimum sum for the current element
                min_sum = float('inf')
                
                # Iterate through each column in the previous row
                for k in range(n):
                    # Skip if choosing the same column in adjacent rows
                    if j != k:
                        # Update the minimum sum
                        min_sum = min(min_sum, grid[i-1][k])
                
                # Update the current element with the minimum sum
                grid[i][j] += min_sum
        
        # Return the minimum sum from the last row
        return min(grid[-1])
