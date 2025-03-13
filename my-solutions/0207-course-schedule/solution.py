from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * (numCourses)
        for i in prerequisites:
            graph[i[1]].append(i[0])
            in_degree[i[0]] += 1
        cnt =0 
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
                cnt += 1

        while q:
            course = q.popleft()
            for next_course in graph[course]:
                in_degree[next_course] -= 1  # 선수 과목을 하나 들었으니 감소
                if in_degree[next_course] == 0:  # 이제 들을 수 있는 상태면 큐에 추가
                    q.append(next_course)

                    cnt += 1
        if cnt == numCourses:
            return True

        else:
            return False
