class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        temp = 0
        ans = []
        for i in range(n):
            temp = temp * 2 + nums[i]
            if temp % 5  == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans
