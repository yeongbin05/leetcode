from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        q = deque()
        ans = [0] * n
        for i in range(n):
            while q and q[-1][0] < temperatures[i]:
                ans[q[-1][1]] = i - q[-1][-1]
                q.pop()

            q.append([temperatures[i],i])


        return ans
