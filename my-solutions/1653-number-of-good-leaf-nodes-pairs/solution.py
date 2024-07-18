# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                # Leaf node, return distance 0
                return [1]
            
            leftDistances = dfs(node.left)
            rightDistances = dfs(node.right)
            
            # Count good pairs between left and right distances
            nonlocal result
            for l in leftDistances:
                for r in rightDistances:
                    if l + r <= distance:
                        result += 1
            
            # Increment distances by 1 for the parent call
            return [d + 1 for d in leftDistances + rightDistances]
        
        result = 0
        dfs(root)
        return result
