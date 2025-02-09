from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(row,col,flag):
            q = deque([(row,col)])
            if flag == 'p':
                can_visit_p[row][col] = 1
                while q:
                    ci,cj = q.popleft()
                    for di,dj in ((0,-1),(0,1),(1,0),(-1,0)):
                        ni,nj = ci+di,cj+dj
                        if 0<=ni<m and 0<=nj<n and can_visit_p[ni][nj] == 0 and heights[ni][nj] >= heights[ci][cj]:
                            q.append((ni,nj))
                            can_visit_p[ni][nj] = 1

                

            else:
                can_visit_a[row][col] = 1
                while q:
                    ci,cj = q.popleft()
                    for di,dj in ((0,-1),(0,1),(1,0),(-1,0)):
                        ni,nj = ci+di,cj+dj
                        if 0<=ni<m and 0<=nj<n and can_visit_a[ni][nj] == 0 and heights[ni][nj] >= heights[ci][cj]:
                            q.append((ni,nj))
                            can_visit_a[ni][nj] = 1
                            

            


        ans = []
        m,n = len(heights),len(heights[0])
        can_visit_p = [[0]*n for _ in range(m)]
        can_visit_a = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:

                    if i == 0  or j == 0:
                        flag = 'p'
                        bfs(i,j,flag)
                    # 두 범위에 모두 들어가는 경우도 있어서 둘다 if문
                    if i == m-1 or j == n-1:
                        flag = 'a'
                        bfs(i,j,flag)
        for i in range(m):
            for j in range(n):
                if can_visit_p[i][j] and can_visit_a[i][j]:
                    ans.append([i,j])
        return ans
