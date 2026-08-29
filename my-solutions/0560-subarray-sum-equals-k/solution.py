class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        pre = [0] * (n+1)
        for i in range(1,n+1):
            pre[i] = pre[i-1] + nums[i-1]

        
        frequency = {0:1,}
        for i in range(1,n+1):
            if pre[i]-k in frequency:
                ans += frequency[pre[i]-k]
            if pre[i] in frequency:
                frequency[pre[i]] += 1
            else:
                frequency[pre[i]] = 1
        return ans
                

