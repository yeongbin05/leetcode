class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        not_zero = []
        cnt = 0
        n = len(nums)
        for i in range(n):
            if i != n-1:
                if nums[i] == nums[i+1]:
                    nums[i] *= 2
                    nums[i+1] = 0
            if nums[i] != 0 :
                not_zero.append(nums[i])
                cnt += 1
        
        for i in range(n-cnt):
            not_zero.append(0)

        return not_zero

