# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startValue, destValue):
        def findLCA(node):
            if not node or node.val in (startValue, destValue):
                return node
            left = findLCA(node.left)
            right = findLCA(node.right)
            if left and right:
                return node
            return left if left else right

        def dfs(node, parent=None):
            if node:
                if parent:
                    parent_map[node.val] = parent
                dfs(node.left, node)
                dfs(node.right, node)

        parent_map = {}
        dfs(root)
        
        lca = findLCA(root)
        
        start_path = []
        dest_path = []
        
        node = startValue
        while node != lca.val:
            start_path.append('U')
            node = parent_map[node].val
        
        def getPathToDescendant(lca, target):
            path = []
            stack = [(lca, "")]
            while stack:
                node, cur_path = stack.pop()
                if node.val == target:
                    return cur_path
                if node.left:
                    stack.append((node.left, cur_path + "L"))
                if node.right:
                    stack.append((node.right, cur_path + "R"))
        
        dest_path = getPathToDescendant(lca, destValue)
        
        return ''.join(start_path) + dest_path
            
