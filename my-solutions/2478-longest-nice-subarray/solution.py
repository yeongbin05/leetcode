class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        window = 0
        max_length = 0

        for right in range(len(nums)):
            while (window & nums[right]) != 0:
                window ^= nums[left]
                left += 1
            window |= nums[right]
            max_length = max(max_length, right - left + 1)
        
        return max_length
