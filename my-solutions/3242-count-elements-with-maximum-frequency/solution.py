class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_frequency = {}
        max_frequency = 0
        ans = 0
        for i in nums:
            if i in nums_frequency:
                nums_frequency[i] += 1

            else:
                nums_frequency[i] = 1
            if nums_frequency[i] > max_frequency:
                    max_frequency = nums_frequency[i]
        
        for i in nums_frequency:
            if nums_frequency[i] == max_frequency:
                ans += max_frequency

        return ans
