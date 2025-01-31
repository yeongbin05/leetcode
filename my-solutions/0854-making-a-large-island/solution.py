from collections import deque
from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def bfs(row, col, island_id):
            """(row, col)에서 시작하는 섬을 BFS로 탐색하고, 해당 섬의 크기를 반환"""
            temp = [(row, col)]
            q = deque([(row, col)])
            grid[row][col] = island_id  # 해당 섬을 island_id로 마킹
            size = 1  # 섬의 크기

            while q:
                ci, cj = q.popleft()
                for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                        q.append((ni, nj))
                        grid[ni][nj] = island_id  # 같은 섬으로 표시
                        size += 1
                        temp.append((ni, nj))
            return size
        
        n = len(grid)
        island_sizes = {0: 0}  # 섬의 id별 크기 저장 (0은 빈칸)
        island_id = 2  # 섬 id는 2부터 시작 (1과 0은 이미 사용됨)

        # Step 1: 각 섬을 BFS로 탐색하여 island_sizes에 기록
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = bfs(i, j, island_id)
                    island_id += 1

        # Step 2: 기존 섬 중 가장 큰 크기 저장
        max_size = max(island_sizes.values())

        # Step 3: 각 0을 1로 바꿨을 때 연결될 수 있는 섬들의 크기 합산
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    total_size = 1  # 현재 0을 1로 바꾸므로 기본 크기 1

                    # 4방향 탐색하여 인접한 섬들의 크기 합산
                    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            seen.add(grid[ni][nj])  # 같은 섬 중복 방지

                    for island in seen:
                        total_size += island_sizes[island]

                    # 최대 섬 크기 갱신
                    max_size = max(max_size, total_size)

        return max_size

