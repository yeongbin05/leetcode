from collections import deque
import heapq
class Solution(object):
    def maxMatrixSum(self, matrix):
        heap = []
        n = len(matrix)
        m = len(matrix[0])
        cnt = 0 
        Sum = 0
        least = 100001
        for i in range(n):
            for j in range(m):
                Sum += abs(matrix[i][j])
                
                if matrix[i][j] <= 0 :
                    cnt += 1
                if abs(matrix[i][j]) < least:
                    least = abs(matrix[i][j])

        if cnt % 2 ==0:
            return Sum

        else:
            return Sum - abs(least) * 2
    
