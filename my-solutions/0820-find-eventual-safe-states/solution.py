from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        
        # 역방향 그래프 생성
        reverse_graph = [[] for _ in range(n)]
        indegree = [0] * n  # 진입 차수 배열
        
        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)  # 간선 방향을 반대로
                indegree[u] += 1  # 원래 그래프의 진입 차수 계산

        # 진입 차수가 0인 노드들을 초기 큐에 추가
        queue = deque([i for i in range(n) if indegree[i] == 0])
        safe_nodes = []

        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            
            # 역방향 그래프에서 현재 노드 제거
            for neighbor in reverse_graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:  # 새롭게 진입 차수가 0이 된 노드
                    queue.append(neighbor)

        return sorted(safe_nodes)  # 안전한 노드를 정렬하여 반환

