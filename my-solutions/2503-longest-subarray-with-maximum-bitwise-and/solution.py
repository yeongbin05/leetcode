class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = max(nums)
        ans = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == k :
                temp += 1
            else : 
                temp = 0
            if temp > ans :
                ans = temp
        return ans
