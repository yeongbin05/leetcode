class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        # 우상향인지 좌하향인지
        up_right = True
        down_left = False
        row,col = 0,0
        m,n = len(mat[0]),len(mat)
        for i in range(m*n):

            ans.append(mat[row][col])
            if up_right == True :
                if row == 0:
                    col += 1
                    if col >= m :
                        col -= 1
                        row += 1
                    up_right = False
                    down_left = True
                elif col >= m-1 :
                    row += 1
                    up_right = False
                    down_left = True
                else:
                    row -= 1
                    col += 1

            elif down_left == True:
                if col == 0:
                    row += 1
                    if row >= n :
                        row -= 1
                        col += 1
                    up_right = True
                    down_left = False
                elif row >= n-1 :
                    col += 1
                    up_right = True
                    down_left = False
                else:
                    row += 1
                    col -= 1
        return ans
            


