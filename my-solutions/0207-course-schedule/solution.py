from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)   # b -> a

        # 상태 배열
        state = [0] * numCourses

        def dfs(node):
            # 현재 경로에 다시 들어오면 사이클
            if state[node] == 1:
                return False

            # 이미 안전하다고 검증된 노드
            if state[node] == 2:
                return True

            # 탐색 시작
            state[node] = 1

            for nxt in graph[node]:
                if not dfs(nxt):
                    return False

            # 탐색 완료
            state[node] = 2
            return True

        # 모든 노드 검사
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
