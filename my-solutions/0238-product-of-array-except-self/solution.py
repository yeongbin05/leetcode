class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left,right  = [0] * n, [0] * n
        prefix,suffix = 1, 1
        for i in range(n):
            left[i] = nums[i] * prefix
            prefix = left[i]
        for i in range(n-1,-1,-1):
            right[i] = nums[i] * suffix
            suffix = right[i]
        
        ans = [0] * n
        for i in range(n):
            if i == 0:
                ans[i] = right[i+1]
            elif i == n-1:
                ans[i] = left[i-1]
            
            else:
                ans[i] = left[i-1] * right[i+1]

        return ans


