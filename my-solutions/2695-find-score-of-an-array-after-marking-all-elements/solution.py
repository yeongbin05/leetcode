import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        # 우선순위 큐에 초기 값을 모두 삽입
        hq = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(hq)
        
        visited = [False] * n
        ans = 0

        while hq:
            val, idx = heapq.heappop(hq)

            # 이미 방문한 인덱스는 무시
            if visited[idx]:
                continue

            # 점수에 현재 값 추가
            ans += val

            # 현재 인덱스와 인접 인덱스 방문 처리
            visited[idx] = True
            if idx > 0:
                visited[idx - 1] = True
            if idx < n - 1:
                visited[idx + 1] = True

        return ans

