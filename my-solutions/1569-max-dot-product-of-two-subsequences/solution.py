class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1),len(nums2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for row in range(1,m+1):
            for col in range(1,n+1):
                # nums1,nums2에 col-1,row-1하는 이유는 dp는 n,m보다 1씩 크게 만들었기때문에
                dp[row][col] = max(dp[row-1][col-1]+nums1[col-1]*nums2[row-1], dp[row-1][col],dp[row][col-1])
     
        # for i in dp:
        #     print(i)
        ans = max(dp)[-1]
        if ans == 0:
            ans = -float('inf')
            for i in range(n):
                for j in range(m):
                    if nums1[i] * nums2[j] > ans:
                        ans = nums1[i] * nums2[j]
        
        return ans
       
