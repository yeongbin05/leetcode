from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 그래프 초기화 및 진입 차수 계산
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            in_degree[b] += 1
        
        # 위상 정렬
        topo_order = []
        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        while q:
            node = q.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        
        # 각 노드에서 도달 가능한 노드 계산
        reachable = [set() for _ in range(numCourses)]
        for node in reversed(topo_order):
            for neighbor in graph[node]:
                reachable[node].add(neighbor)
                reachable[node].update(reachable[neighbor])
        
        # 쿼리 응답
        return [v in reachable[u] for u, v in queries]

