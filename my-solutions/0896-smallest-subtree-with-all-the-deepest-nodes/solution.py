# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            # returns (depth, ans_node)
            if not node:
                return (0, None)

            ld, la = dfs(node.left)
            rd, ra = dfs(node.right)

            if ld == rd:
                return (ld + 1, node)     # deepest nodes exist in both sides equally -> LCA is node
            elif ld > rd:
                return (ld + 1, la)       # left side deeper -> answer is left's answer
            else:
                return (rd + 1, ra)       # right side deeper -> answer is right's answer

        return dfs(root)[1]
