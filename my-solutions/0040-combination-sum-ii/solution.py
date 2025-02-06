from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()  # 중복 방지를 위해 정렬

        def backtrack(start, path, total):
            if total == target:
                ans.append(path[:])  # 정답 추가
                return
            if total > target:
                return  # 가지치기 (Pruning)

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:  # 중복 방지
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])  # i+1로 호출 (한 번만 사용 가능)
                path.pop()  # 백트래킹

        backtrack(0, [], 0)
        return ans

