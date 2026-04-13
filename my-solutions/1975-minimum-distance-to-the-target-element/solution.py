class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = 10001
        for idx,val in enumerate(nums):
            if val == target:
                ans = min(ans,abs(idx-start))

        return ans
