class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for idx,val in enumerate(temperatures):
            while stack and val > stack[-1][1]:
                left_idx,left_val = stack.pop()
                ans[left_idx] = idx - left_idx
            stack.append((idx,val))

        return ans
