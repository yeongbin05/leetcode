import heapq
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        hq = []
        for i in gifts:
            heapq.heappush(hq,-i)

        for i in range(k):
            x = heapq.heappop(hq)
            heapq.heappush(hq,-int((-x)**(1/2)))
            
        
        return sum([-i for i in hq])
