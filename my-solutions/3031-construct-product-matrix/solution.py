class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n,m = len(grid),len(grid[0])
        p,prefix,suffix = [[0]*m for _ in range(n)],[[0]*m for _ in range(n)],[[0]*m for _ in range(n)]
        
        product = 1
        for row in range(n):
            for col in range(m):
                prefix[row][col] = product
                product = (product * grid[row][col]) % 12345
        


        product = 1
        for row in range(n-1,-1,-1):
            for col in range(m-1,-1,-1):
                suffix[row][col] = product
                product = (product * grid[row][col]) % 12345
        
        for i in range(n):
            for j in range(m):
                p[i][j] = (prefix[i][j] * suffix[i][j]) % 12345

        


        return p
