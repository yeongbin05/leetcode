from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(row,col):
            q = deque([(row,col)])
            visited[row][col] = 1
            area = 1
            while q:
                ci,cj = q.popleft()
                for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
                    ni,nj = ci+di,cj+dj
                    if 0<=ni<m and 0<=nj<n and grid[ni][nj] == 1 and visited[ni][nj] == 0:
                        q.append((ni, nj))
                        area += 1
                        visited[ni][nj] = 1
            return area
        m,n = len(grid),len(grid[0])
        visited = [[0]*n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    temp = bfs(i,j)
                    if temp > ans :
                        ans = temp

        return ans
