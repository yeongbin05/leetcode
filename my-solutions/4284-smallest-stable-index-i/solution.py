class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_nums,min_nums = [0]*n,[0]*n
        max_num = 0 
        min_num = float('inf')
        for i in range(n):
            max_nums[i] = max(nums[i],max_num)
            max_num = max_nums[i]
        for i in range(n-1,-1,-1):
            print(i)
            min_nums[i] = min(nums[i],min_num)
            min_num = min_nums[i]


        for i in range(n):
            if max_nums[i] - min_nums[i] <= k:
                return i


        return -1
