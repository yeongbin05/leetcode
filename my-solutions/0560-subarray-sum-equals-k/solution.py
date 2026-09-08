class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dic = {0:1}
        pre = [0] * (n+1)
        ans = 0
        for i in range(1,n+1):
            pre[i] = pre[i-1] + nums[i-1]
            if pre[i]-k in dic:
                ans += dic[pre[i]-k]

            if pre[i] in dic:
                dic[pre[i]]  += 1
            else:
                dic[pre[i]] = 1

        return ans
