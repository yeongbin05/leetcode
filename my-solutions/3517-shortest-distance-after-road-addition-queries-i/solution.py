import heapq
from typing import List

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # 초기 그래프 설정: 0 -> 1 -> 2 -> ... -> n-1
        graph = {i: [i + 1] for i in range(n - 1)}
        graph[n - 1] = []  # 마지막 노드는 연결 없음

        def dijkstra() -> int:
            distances = [float('inf')] * n
            distances[0] = 0
            pq = [(0, 0)]  # (distance, node)

            while pq:
                dist, node = heapq.heappop(pq)
                if node == n - 1:
                    return dist
                if dist > distances[node]:
                    continue
                for neighbor in graph[node]:
                    new_dist = dist + 1
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        heapq.heappush(pq, (new_dist, neighbor))
            return -1  # 도달 불가 시

        answer = []
        for u, v in queries:
            if v not in graph[u]:
                graph[u].append(v)
            answer.append(dijkstra())

        return answer

