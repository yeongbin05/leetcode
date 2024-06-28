class Solution(object):
    def maximumImportance(self, n, roads):
        degree = [0] * n
        for road in roads:
            degree[road[0]] += 1
            degree[road[1]] += 1

        # 2단계: 도시를 차수에 따라 내림차순으로 정렬합니다.
        sorted_cities = sorted(range(n), key=lambda x: degree[x], reverse=True)

        # 3단계: 차수에 따라 높은 값에서 낮은 값 순으로 값을 할당합니다.
        value = [0] * n
        for i in range(n):
            value[sorted_cities[i]] = n - i

        # 4단계: 모든 도로의 총 중요성을 계산합니다.
        total_importance = 0
        for road in roads:
            total_importance += value[road[0]] + value[road[1]]

        return total_importance
