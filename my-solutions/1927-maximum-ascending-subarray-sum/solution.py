class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        temp = nums[0]
        n = len(nums)
        ans = temp
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                temp += nums[i]
            else:
                temp = nums[i]
            
            if temp > ans:
                ans = temp

        return ans
