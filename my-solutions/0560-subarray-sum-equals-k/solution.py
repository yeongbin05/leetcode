class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        seen = {0 : 1}

        temp = 0
        for i in nums:
            temp += i
            if temp - k in seen:
                ans += seen[temp-k]
            if temp in seen:
                seen[temp] += 1
            else:
                seen[temp] = 1
        return ans
