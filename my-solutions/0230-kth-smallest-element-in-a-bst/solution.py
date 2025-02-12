# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        hq = []
        def recur(node):
            if not node:
                return
            heapq.heappush(hq,node.val)
            return recur(node.left), recur(node.right)


        recur(root)
        for i in range(k-1):
            heapq.heappop(hq)

        return heapq.heappop(hq)

