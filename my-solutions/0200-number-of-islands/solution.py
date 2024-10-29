from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def bfs(row,col):
            visited[row][col] = True
            q = deque([(row,col)])
            while q:
                ci,cj = q.popleft()
                for di,dj in ((0,1),(0,-1),(1,0),(-1,0)) :
                    ni = ci + di
                    nj = cj + dj
                
                    if 0<=ni<m and 0<=nj<n and not visited[ni][nj]  and grid[ni][nj] == "1":
                        q.append((ni,nj))
                        visited[ni][nj] = True

        visited = [[False]*n for _ in range(m)]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j]  and grid[i][j] == "1":
                    bfs(i,j)
                    ans += 1
                    
        
        return ans
