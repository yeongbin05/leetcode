class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(target), len(words[0])
        
        # Step 1: Precompute character frequencies for each column
        column_freq = [{} for _ in range(n)]
        for word in words:
            for j, char in enumerate(word):
                column_freq[j][char] = column_freq[j].get(char, 0) + 1

        # Step 2: Initialize DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(n + 1):
            dp[0][j] = 1  # Base case: empty target

        # Step 3: Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Case 1: Do not use the current column
                dp[i][j] = dp[i][j - 1]
                
                # Case 2: Use the current column
                if target[i - 1] in column_freq[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1] * column_freq[j - 1][target[i - 1]]
                    dp[i][j] %= MOD

        return dp[m][n]
