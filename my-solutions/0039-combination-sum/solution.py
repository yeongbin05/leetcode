class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def comb(idx,target):
            if target == 0:
                # print(temp)
                ans.append(list(temp))
            elif target < 0 :
                return
            for i in range(idx,n):
                temp.append(candidates[i])
                comb(i,target-candidates[i])
                temp.pop()
        ans = []
        n = len(candidates)
        temp = []
        comb(0,target)

        return ans

