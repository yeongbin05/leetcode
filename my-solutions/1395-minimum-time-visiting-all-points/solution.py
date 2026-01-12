class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for i in range(n-1):
            cur,next = points[i],points[i+1]
            ans += max(abs(cur[0]-next[0]),abs(cur[1]-next[1]))

        return ans
