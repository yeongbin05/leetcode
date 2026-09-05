class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def recur(temp):
            if len(temp) == n:
                ans.append(temp[:])
                return
            for i in nums:
                if i not in temp:
                    temp.append(i) 
                    recur(temp)
                    temp.pop()


        recur([])



        return ans
