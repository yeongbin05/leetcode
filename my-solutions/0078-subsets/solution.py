class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def comb(idx,temp):
            if len(temp) <= n:
                ans.append(temp[:])

            for i in range(idx,n):
                temp.append(nums[i])
                comb(i+1,temp)
                temp.pop()

        comb(0,[])
        return ans
