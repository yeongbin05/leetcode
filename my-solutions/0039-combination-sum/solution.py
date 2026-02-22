class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def back(idx,temp):
            if sum(temp) > target:
                return
            elif sum(temp) == target:
                ans.append(temp[:])
                return

            for i in range(idx,len(candidates)):
                temp.append(candidates[i])
                back(i,temp)
                temp.pop()
        back(0,[])

        return ans
