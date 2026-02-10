from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs , visited체크
        m , n = len(grid),len(grid[0])
        visited = [[0]*n for _ in range(m)]
        ans = 0
        def bfs(row,col):
            q = deque([(row,col)])
            visited[row][col] =  1
            while q:
                ci,cj = q.popleft()
                for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
                    ni,nj = ci+di, cj+dj
                    if 0<=ni<m and 0<=nj<n and not visited[ni][nj] and grid[ni][nj] == "1":
                        visited[ni][nj] = 1
                        q.append((ni, nj))


        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and not visited[row][col]:
                    bfs(row,col)
                    ans += 1
        return ans

