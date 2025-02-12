class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n+1)

        for i in range(1,n+1):
            for j in range(i,n+1):
                if nums[j-1] > nums[i-1]:
                    dp[j] = max(dp[j],dp[i]+1)
        

        return max(dp)
