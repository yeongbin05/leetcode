import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        ans = []
        for i in points:
            heapq.heappush(hq,(i[0]**2+i[1]**2,i))

        for i in range(k):
            ans.append(heapq.heappop(hq)[1])
        return ans

