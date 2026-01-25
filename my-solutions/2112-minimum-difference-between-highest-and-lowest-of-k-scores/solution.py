class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        ans = float('inf')
        for i in range(n-k+1):
            if nums[i+k-1] - nums[i] < ans:
                ans = nums[i+k-1] - nums[i]
        return ans
