class Solution:
    def check(self, nums: List[int]) -> bool:
        ans = sorted(nums)
        if nums == ans:
            return True

        for i in range(len(nums)):
            if nums[i:] + nums[:i] == ans:
                return True



        return False
