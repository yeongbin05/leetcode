class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            nums = [0] * 10
            for col in range(9):
                if board[row][col] == '.':
                    continue
                nums[int(board[row][col])] += 1
                if nums[int(board[row][col])] > 1:
                    return False

        for col in range(9):
            nums = [0] * 10
            for row in range(9):
                if board[row][col] == '.':
                    continue
                nums[int(board[row][col])] += 1
                if nums[int(board[row][col])] > 1:
                    return False
            print(nums)
        
        for row in range(0,9,3):
            for col in range(0,9,3):
                nums = [0] * 10
                for i in range(row,row+3):
                    for j in range(col,col+3):
                        if board[i][j] == '.':
                            continue
                        nums[int(board[i][j])] += 1
                        if nums[int(board[i][j])] > 1:
                            return False
        return True
