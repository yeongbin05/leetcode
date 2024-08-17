class Solution(object):
    def maxPoints(self, points):
        m, n = len(points), len(points[0])

        # 이전 행의 최대 점수를 저장할 dp 배열
        dp = points[0][:]

        for i in range(1, m):
            # 왼쪽에서 오른쪽으로 가면서 현재 행의 잠정 최대값을 계산
            left_max = [0] * n
            left_max[0] = dp[0]
            for j in range(1, n):
                left_max[j] = max(left_max[j-1] - 1, dp[j])

            # 오른쪽에서 왼쪽으로 가면서 현재 행의 잠정 최대값을 계산
            right_max = [0] * n
            right_max[-1] = dp[-1]
            for j in range(n-2, -1, -1):
                right_max[j] = max(right_max[j+1] - 1, dp[j])

            # 현재 행의 각 셀에 대해 최대 점수를 계산
            for j in range(n):
                dp[j] = points[i][j] + max(left_max[j], right_max[j])

        return max(dp)
        
