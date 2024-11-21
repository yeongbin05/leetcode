class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        board = [[0]*n for _ in range(m)]
        for r, c in guards:
            board[r][c] = 'G'
        for r, c in walls:
            board[r][c] = 'W'
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Mark guarded cells
        for r, c in guards:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n and board[nr][nc] not in ('W', 'G'):
                    if board[nr][nc] == 0:  # Mark as guarded only if it was unguarded
                        board[nr][nc] = 1
                    nr += dr
                    nc += dc

        
        ans = sum(1 for i in range(m) for j in range(n) if board[i][j] == 0)
        
        return ans
