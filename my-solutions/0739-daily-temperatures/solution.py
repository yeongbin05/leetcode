class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n
        for idx,val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                ans[stack[-1]] = idx - stack[-1]
                stack.pop()
            
            stack.append(idx)

        return ans
