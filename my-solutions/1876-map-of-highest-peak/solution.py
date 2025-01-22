import heapq
from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        hq = []
        m,n = len(isWater),len(isWater[0])
        visited = [[0] * n for _ in range(m)]
        ans = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    heapq.heappush(hq,(0,i,j))
                    visited[i][j] = 1
        print(hq)
        while hq:
                height,ci,cj = heapq.heappop(hq)
                for di,dj in ((0,1),(0,-1),(1,0),(-1,0)):
                    ni,nj = ci+di,cj+dj
                    if 0<=ni<m and 0<=nj<n and visited[ni][nj] == 0 :
                        ans[ni][nj] = height + 1
                        visited[ni][nj] = 1
                        heapq.heappush(hq,(height+1,ni,nj))
        


        return ans
