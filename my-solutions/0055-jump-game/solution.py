class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        can_reach = [0] * (n)
        can_reach[0] = 1
        for i in range(n):
            if can_reach[i] == 0:
                return False
            for j in range(1,nums[i]+1):
            
                if i + j == n-1:
                    return True
                elif i+j<n:
                    can_reach[i+j] = 1
                        
