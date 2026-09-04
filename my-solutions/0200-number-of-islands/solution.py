from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(row,col):
            visited[row][col] = 1
            q = deque([(row,col)])

            while q:
                ci,cj = q.popleft()
                for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                    ni,nj = ci + di , cj + dj
                    if 0<=nj<n and 0<=ni<m and grid[ni][nj] == '1' and visited[ni][nj] == 0  :
                        q.append((ni,nj))
                        visited[ni][nj] = True


        ans = 0
        n,m = len(grid[0]),len(grid)
        visited = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    bfs(i,j)
                    ans += 1

        return ans

