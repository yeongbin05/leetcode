class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):
        # 프로젝트들을 자본(capital)을 기준으로 정렬합니다.
        projects = sorted(zip(capital, profits))
        
        max_heap = []
        project_index = 0
        n = len(profits)
        
        for _ in range(k):
            # 현재 자본으로 시작할 수 있는 모든 프로젝트를 최대 힙에 추가합니다.
            while project_index < n and projects[project_index][0] <= w:
                heapq.heappush(max_heap, -projects[project_index][1])
                project_index += 1
            
            # 시작할 수 있는 프로젝트가 없으면 종료합니다.
            if not max_heap:
                break
            
            # 최대 힙에서 가장 큰 순이익을 가진 프로젝트를 선택하여 완료합니다.
            w += -heapq.heappop(max_heap)
        
        return w
        
