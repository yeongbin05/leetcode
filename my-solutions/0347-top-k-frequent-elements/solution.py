import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == k :
            return nums

        dic = {}
        hq = []
        # hq 길이
        cnt = 0
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for i in dic:
            heapq.heappush(hq,(dic[i],i))
            cnt += 1
            if cnt > k:
                heapq.heappop(hq)
            

        return [i[1] for i in hq]

        
