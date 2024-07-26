class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        
        # 주어진 간선들로부터 초기 거리를 설정
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # 플로이드-워셜 알고리즘
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # 각 도시에서 distanceThreshold 이하로 도달 가능한 도시의 수를 계산
        minReachable = float('inf')
        resultCity = -1
        
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    count += 1
            
            # 가장 적은 수의 도시를 가진 도시를 찾고, 같은 경우 번호가 큰 도시를 선택
            if count <= minReachable:
                minReachable = count
                resultCity = i
        
        return resultCity

        
