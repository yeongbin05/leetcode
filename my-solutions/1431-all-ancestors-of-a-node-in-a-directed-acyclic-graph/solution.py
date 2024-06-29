from collections import defaultdict, deque
class Solution(object):
    def getAncestors(self, n, edges):
        graph = defaultdict(list)
        indegree = [0] * n

        # Fill the graph and indegree array
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # List to store ancestors for each node
        ancestors = [set() for _ in range(n)]

        # Queue for nodes with no incoming edges
        queue = deque([i for i in range(n) if indegree[i] == 0])

        # Topological sort
        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                # Add current node's ancestors to neighbor's ancestors
                ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Convert sets to sorted lists
        return [sorted(list(ancestor_set)) for ancestor_set in ancestors]
        
