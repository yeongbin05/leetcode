class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)

        cnt = 1
        while cnt < k:
            heapq.heappop(heap)
            cnt += 1

        return -heapq.heappop(heap)
