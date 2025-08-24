class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if sum(nums) == n:
            return n-1
        left,right = 0,0
        temp = 0
        ans = 0
        for i in range(n):
            if nums[i] == 1:
                temp += 1
            else:
                ans = max(ans,left+temp)
                if left != 0:
                    right = temp
                    left = right
                else:
                    left = temp
                    
                temp = 0
        ans = max(ans,left+temp)
        return ans
