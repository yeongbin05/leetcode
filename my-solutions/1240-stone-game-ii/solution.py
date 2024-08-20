class Solution(object):
    def stoneGameII(self, piles):
        n = len(piles)
    
        # Compute suffix sum array
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
        
        # dp[i][m] will be the maximum number of stones Alice can get starting from i with M = m
        dp = [[0] * (n + 1) for _ in range(n)]
        
        def dp_func(i, m):
            if i == n:
                return 0
            if dp[i][m] != 0:
                return dp[i][m]
            max_stones = 0
            for x in range(1, 2 * m + 1):
                if i + x > n:
                    break
                max_stones = max(max_stones, suffix_sum[i] - dp_func(i + x, max(m, x)))
            dp[i][m] = max_stones
            return max_stones
        
        return dp_func(0, 1)

