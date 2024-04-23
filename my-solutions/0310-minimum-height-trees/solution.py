from collections import defaultdict, deque
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]  # Only one node, return the root
            
        # Create adjacency list
        adj_list = defaultdict(set)
        for u, v in edges:
            adj_list[u].add(v)
            adj_list[v].add(u)
            
        # Initialize queue with leaf nodes
        leaves = deque([node for node in range(n) if len(adj_list[node]) == 1])
        
        # Remove leaves level by level
        while n > 2:
            n -= len(leaves)
            new_leaves = deque()
            
            # Remove current leaves and update adjacency list
            while leaves:
                leaf = leaves.popleft()
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)
                
                # If neighbor becomes a leaf, add to new_leaves
                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
                    
            leaves = new_leaves
            
        # The remaining nodes in leaves are the roots of MHTs
        return list(leaves)
            
