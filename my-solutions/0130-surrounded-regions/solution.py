from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def bfs(row,col):
            # edge에 안 닿는다
            flag = True
            temp = [(row,col)]
            q = deque([(row,col)])
            visited[row][col] = 1
            while q :
                ci,cj = q.popleft()
                for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
                    ni,nj = ci+di,cj+dj
                    if 0<=ni<m and 0<=nj<n and board[ni][nj] == 'O' and visited[ni][nj] == 0:
                        q.append((ni,nj))
                        visited[ni][nj] = 1
                        temp.append((ni,nj))
                    elif ni < 0 or ni >= m or nj < 0 or nj >= n :
                        # edge에 닿는다
                        flag = False
            if flag == True:
                for i,j in temp:
                    board[i][j] = 'X'
        m,n = len(board),len(board[0])
        visited = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and visited[i][j] == 0:
                    bfs(i,j)
