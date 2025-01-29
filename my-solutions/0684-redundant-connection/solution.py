class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])  # 경로 압축(Path compression)
            return parent[x]
        
        def union(parent, rank, x, y):
            rootX = find(parent, x)
            rootY = find(parent, y)
            if rootX == rootY:
                return False  # 이미 같은 집합에 속해 있음 → 사이클 발생
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
            return True
        
        n = len(edges)
        parent = list(range(n + 1))
        rank = [0] * (n + 1)
        
        for u, v in edges:
            if not union(parent, rank, u, v):
                return [u, v] 
