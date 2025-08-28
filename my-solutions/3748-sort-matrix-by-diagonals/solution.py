class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        # 밑에서 두번째줄부터
        temp_row = n-1
        row = n-2
        for i in range(n-1):
            temp_row -= 1
            row = temp_row
            col = 0
            temp = []
            while 0<=row<n and 0<=col<n:
                temp.append(grid[row][col])
                row += 1
                col += 1
            row -= 1
            col -= 1
            temp.sort(reverse=True)
            while col >= 0:
                grid[row][col] = temp.pop()
                row -= 1
                col -=1

        temp_col = 0
        col = 0
        for i in range(n-2):
            temp_col += 1
            col = temp_col
            row = 0
            temp = []
            while 0<=row<n and 0<=col<n:
                temp.append(grid[row][col])
                row += 1
                col += 1
            row -= 1
            col -= 1
            temp.sort()
            while row >= 0:
                grid[row][col] = temp.pop()
                row -= 1
                col -=1

            
        return grid

