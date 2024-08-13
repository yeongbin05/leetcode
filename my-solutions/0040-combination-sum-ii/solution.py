class Solution(object):
    def combinationSum2(self, candidates, target):
        
        def backtrack(start, target, path):
        
            if target == 0:
                res.append(path)
                return
            
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        candidates.sort()  
        res = []
        backtrack(0, target, [])
        return res

