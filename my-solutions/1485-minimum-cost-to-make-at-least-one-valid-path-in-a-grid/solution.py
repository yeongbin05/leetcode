from collections import deque
import heapq  # 우선순위 큐를 위해 사용

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        # cost,row,col
        hq = [(0,0,0)]
        visited = [[float('inf')] * n for _ in range(m)]
        visited[0][0] = 0
        while hq:
            cost,ci,cj = heapq.heappop(hq)
            if ci == m - 1 and cj == n - 1:
                return cost
            for i,(di,dj) in enumerate(directions):
                ni = ci + di
                nj = cj + dj

                if 0<=ni<m and 0<=nj<n:
                    if grid[ci][cj] == i + 1:
                        next_cost = cost
                    else:
                        next_cost = cost + 1
                    if next_cost < visited[ni][nj] :
                        visited[ni][nj] = next_cost
                        heapq.heappush(hq,(next_cost,ni,nj))

        return -1
