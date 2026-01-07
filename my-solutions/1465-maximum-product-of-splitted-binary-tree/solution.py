# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        sums = []

        def sub_sum(node):
            if not node:
                return 0
            s = node.val + sub_sum(node.left) + sub_sum(node.right)
            sums.append(s)  # 원본 node.val 안 바꿈
            return s

        total = sub_sum(root)

        best = 0
        for s in sums:
            best = max(best, s * (total - s))

        return best % MOD
