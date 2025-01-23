class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        def bfs(row,col,ans):
            print(ans,'ans')
            nj = col
            # 우측
            while 1:
                nj += 1
                if nj >= n :
                    break
                if grid[row][nj] == 1 and visited[row][nj] == 0:
                    print(1111)
                    ans += 1
                    visited[row][nj] = 1
            nj = col
            # 좌측
            while 1:
                nj -= 1
                if nj < 0 :
                    break
                if grid[row][nj] == 1 and visited[row][nj] == 0:
                    ans += 1
                    visited[row][nj] = 1
            ni = row
            # 위쪽
            while 1:
                ni += 1
                if ni >= m :
                    break
                if grid[ni][col] == 1 and visited[ni][col] == 0:
                    ans += 1
                    visited[ni][col] = 1
            ni = row
            # 아래쪽
            while 1:
                ni -= 1
                if ni < 0:
                    break
                if grid[ni][col] == 1 and visited[ni][col] == 0:
                    ans += 1
                    visited[ni][col] = 1
            return ans
        ans = 0
        m,n = len(grid),len(grid[0])
        visited = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 :
                    ans += bfs(i,j,0)
                    

        return ans
