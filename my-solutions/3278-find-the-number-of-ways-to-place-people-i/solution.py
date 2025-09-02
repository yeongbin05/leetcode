class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        cnt = 0
        for i in range(n):
            for j in range(n):
                if i!= j and points[i][0] <= points[j][0] and points[i][1] >= points[j][1]:
                    for k in range(n):
                        if points[k] != points[i] and points[k] != points[j]:
                            if points[i][0] <= points[k][0] <= points[j][0] and points[j][1] <= points[k][1] <= points[i][1]:
                                break
                    else:
                        cnt += 1

        return cnt
