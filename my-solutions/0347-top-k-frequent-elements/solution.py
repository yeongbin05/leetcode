import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        ans = []
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        hq = []
        for i in frequency:
            heapq.heappush(hq,(-frequency[i],i))
        for i in range(k):
            ans.append(heapq.heappop(hq)[1])
        

        return ans
