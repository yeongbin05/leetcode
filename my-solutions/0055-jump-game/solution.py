from collections import deque
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        farthest = 0
        for i in range(n):
            if i > farthest:
                return False

            farthest = max(farthest,i + nums[i])
            if farthest >= n-1 :
                return True
