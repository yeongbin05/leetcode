
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p: int, t: int) -> float:
            return (p + 1) / (t + 1) - p / t

        # 최대 힙 생성 (heapq는 기본이 최소힙이라 -를 붙여줌)
        heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(heap)

        # extraStudents명 배정
        for _ in range(extraStudents):
            # 증가량 가장 큰 반 꺼내서
            neg_gain, p, t = heapq.heappop(heap)
            p += 1
            t += 1
            # 갱신된 반 다시 힙에 넣기
            heapq.heappush(heap, (-gain(p, t), p, t))

        # 최종 평균 계산
        total = 0
        while heap:
            _, p, t = heapq.heappop(heap)
            total += p / t

        return total / len(classes)
