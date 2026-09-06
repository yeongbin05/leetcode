class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def recur(temp):
            if len(temp) == n:
                ans.append(temp[:])

            for i in range(n):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    recur(temp)
                    temp.pop()

        recur([])
        return ans
