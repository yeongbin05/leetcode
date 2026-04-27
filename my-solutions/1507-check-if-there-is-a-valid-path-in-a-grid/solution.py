from typing import List
from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        # 각 도로 타입이 연결된 방향
        # (dr, dc)
        dirs = {
            1: [(0, -1), (0, 1)],    # left, right
            2: [(-1, 0), (1, 0)],    # up, down
            3: [(0, -1), (1, 0)],    # left, down
            4: [(0, 1), (1, 0)],     # right, down
            5: [(0, -1), (-1, 0)],   # left, up
            6: [(0, 1), (-1, 0)],    # right, up
        }

        q = deque([(0, 0)])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        while q:
            r, c = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            cur_type = grid[r][c]

            for dr, dc in dirs[cur_type]:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if visited[nr][nc]:
                    continue

                next_type = grid[nr][nc]

                # 다음 칸이 현재 칸 방향으로 다시 연결되어 있어야 함
                if (-dr, -dc) in dirs[next_type]:
                    visited[nr][nc] = True
                    q.append((nr, nc))

        return False
