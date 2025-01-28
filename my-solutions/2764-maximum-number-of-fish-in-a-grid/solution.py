from collections import deque
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def bfs(row,col):
            temp = grid[row][col]
            visited[row][col] = 1
            q = deque([(row,col)])

            while q:
                ci,cj = q.popleft()
                for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
                    ni,nj = ci+di,cj+dj
                    if 0<=ni<m and 0<=nj<n and visited[ni][nj] == 0 and grid[ni][nj] > 0:
                        q.append((ni,nj))
                        visited[ni][nj] = 1
                        temp += grid[ni][nj]

            return temp
        m,n = len(grid),len(grid[0])
        visited = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and visited[i][j] == 0:
                    temp = bfs(i,j)
                    if temp > ans :
                        ans = temp

        return ans
