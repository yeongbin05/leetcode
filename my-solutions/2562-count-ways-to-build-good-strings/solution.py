class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = [0 for _ in range(high+1)]
        dp[0] = 1
        for i in range(1,high+1):
            if i >= zero:
                dp[i] += dp[i-zero]
            if i >= one:
                dp[i] += dp[i-one]
            dp[i] = dp[i] % MOD
        
        return sum(dp[low:high+1]) % MOD
