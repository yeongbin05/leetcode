import heapq
class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        graph = [[] for _ in range(n)]
        for i, (a, b) in enumerate(edges):
            graph[a].append((b, succProb[i]))
            graph[b].append((a, succProb[i]))
        
        # 우선순위 큐 (최대 힙) 사용
        pq = [(-1.0, start_node)]  # (확률, 노드)
        prob = [0.0] * n
        prob[start_node] = 1.0
        
        while pq:
            curr_prob, node = heapq.heappop(pq)
            curr_prob = -curr_prob  # 현재 확률 (양수로 변환)
            
            if node == end_node:
                return curr_prob
            
            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > prob[neighbor]:
                    prob[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))
        
        return 0.0
