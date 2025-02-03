class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        dp_in = [1] * n
        dp_de = [1] * n
        ans = 1
        for i in range(1,n):
            
            if nums[i] > nums[i-1] :
                dp_in[i] = max(dp_in[i],dp_in[i-1] + 1)
                if dp_in[i] > ans:
                    ans = dp_in[i]
            if nums[i] < nums[i-1] :
                dp_de[i] = max(dp_de[i],dp_de[i-1] + 1)
                if dp_de[i] > ans:
                    ans = dp_de[i]

        return ans
