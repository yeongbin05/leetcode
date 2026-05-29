class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')
        for i in nums:
            temp = 0
            i = str(i)
            for j in i:
                temp += int(j)

            if temp < ans :
                ans = temp

        return ans
