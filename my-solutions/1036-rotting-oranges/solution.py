from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        m,n = len(grid),len(grid[0])
        visited = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j,0))
        ans = 0
        while q :
            ci,cj,time = q.popleft()
            for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
                ni,nj = ci+di,cj+dj
                if 0<=ni<m and 0<=nj<n and grid[ni][nj] == 1 and visited[ni][nj] == 0:
                    q.append((ni,nj,time+1))
                    grid[ni][nj] = 2
                    ans = max(ans, time+1)
                    

        for i in grid:
            for j in i:
                if j == 1:
                    return -1

        return ans

