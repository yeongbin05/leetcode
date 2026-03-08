class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        
        left,right = 0,1
        n = len(nums)
        if n == 1:
            return -1
        left = sum(nums[:-1])
        if left == right:
            return n-1

        for i in range(n-2,-1,-1):
            left -= nums[i]
            right *= nums[i+1]
            if left == right:
                return i

        return -1
