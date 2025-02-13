import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        cnt = 0
        while 1:
            x=heapq.heappop(nums)
            if x >= k :
                break
            y=heapq.heappop(nums)
            heapq.heappush(nums,(min(x,y)*2+max(x,y)))

            cnt += 1
        return cnt
