class Solution(object):
    def luckyNumbers (self, matrix):
        
        # arr =[]
        # for i in range(len(matrix)) :
        #     for j in range(len(matrix[0])) :
        #         if matrix[i][j] == min(matrix[i]) and matrix[i][j] == max([matrix[k][j] for k in range(len(matrix))]) :
        #             # print(matrix[i][j],matrix[i],[matrix[k][j] for k in range(len(matrix))])
        #             arr.append(matrix[i][j])

        # return arr
        min_in_rows = {min(row) for row in matrix}
    
        # 각 열의 최대값을 찾습니다.
        max_in_cols = {max(col) for col in zip(*matrix)}
        
        # 행의 최소값이면서 열의 최대값인 숫자를 찾습니다.
        lucky_nums = list(min_in_rows & max_in_cols)
        
        return lucky_nums
