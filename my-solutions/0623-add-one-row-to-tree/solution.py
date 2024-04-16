# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        def dfs(node, current_depth):
            if not node:
                return
            if current_depth == depth - 1:
                left_node = TreeNode(val)
                right_node = TreeNode(val)
                
                left_node.left = node.left
                right_node.right = node.right
                
                node.left = left_node
                node.right = right_node
                return
            
            dfs(node.left, current_depth + 1)
            dfs(node.right, current_depth + 1)

        dfs(root, 1)
        return root
        
