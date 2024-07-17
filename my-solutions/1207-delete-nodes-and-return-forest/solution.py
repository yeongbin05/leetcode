# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        to_delete_set = set(to_delete)
        forest = []

        def dfs(node):
            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in to_delete_set:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return None
            return node

        root = dfs(root)
        if root:
            forest.append(root)
        
        return forest

    # Helper function to build a tree from a list
    def build_tree_from_list(lst):
        if not lst:
            return None
        root = TreeNode(lst[0])
        queue = deque([root])
        i = 1
        while i < len(lst):
            node = queue.popleft()
            if lst[i] is not None:
                node.left = TreeNode(lst[i])
                queue.append(node.left)
            i += 1
            if i < len(lst) and lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
            i += 1
        return root

    def print_forest(forest):
        result = []
        for tree in forest:
            result.append(tree_to_list(tree))
        return result

    def tree_to_list(node):
        if not node:
            return None
        result = []
        queue = deque([node])
        while queue:
            current = queue.popleft()
            if current:
                result.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append(None)
        while result and result[-1] is None:
            result.pop()
        return result
            
