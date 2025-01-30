class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for idx, val in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < val:
                temp = stack.pop()
                ans[temp] = idx - temp
            stack.append(idx)

        return ans
