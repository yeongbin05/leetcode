class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        prefix = [0] * (n+1)
        frequency = {}
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]
        
        for i in range(n+1):
            if (prefix[i] - k ) in frequency:
                ans += frequency[prefix[i]-k]
            if prefix[i] in frequency:
                frequency[prefix[i]] += 1
            else:
                frequency[prefix[i]] = 1
        return ans
