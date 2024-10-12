import heapq
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        # 종료 시간을 저장할 min-heap
        min_heap = []

        for start, end in intervals:
            # 현재 구간의 시작 시간이 가장 빨리 끝나는 구간의 종료 시간보다 크거나 같다면,
            # 해당 구간을 끝낸 것으로 간주하고 heap에서 제거
            if min_heap and min_heap[0] < start:
                heapq.heappop(min_heap)

            # 현재 구간의 종료 시간을 heap에 추가
            heapq.heappush(min_heap, end)

        # heap의 크기가 최소 그룹 수
        return len(min_heap)
