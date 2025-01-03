class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        ans = 0
        prefix = 0
        for i in range(n-1):
            prefix += nums[i]
            total -= nums[i]
            if prefix >= total:
                ans += 1
        return ans
