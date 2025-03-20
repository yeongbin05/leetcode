class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        n = len(candidates)
        def back(idx,temp):
            if sum(temp) == target:
                ans.append(temp[:])
                return
            if sum(temp) > target:
                return
            
            for i in range(idx,n):
                temp.append(candidates[i])
                back(i,temp)
                temp.pop()
        back(0,[])
        return ans
