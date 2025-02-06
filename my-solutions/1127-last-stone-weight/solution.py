import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hq = []
        for i in stones:
            heapq.heappush(hq,-i)
        while len(hq)>1:
            y = -heapq.heappop(hq)
            x = -heapq.heappop(hq)
            if x != y :
                heapq.heappush(hq,-(y-x))
            
        if len(hq) == 0:
            return 0
        else:
            return -hq[0]


