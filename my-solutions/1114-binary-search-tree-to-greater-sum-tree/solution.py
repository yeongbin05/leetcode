# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def bstToGst(self, root):
        self.sum = 0
        self.reverseInOrder(root)
        return root

    def reverseInOrder(self, node):
        if not node:
            return
        # 먼저 오른쪽 서브트리 탐색
        if node.right:
            self.reverseInOrder(node.right)
        # 현재 노드의 값을 누적 합과 더한 값으로 업데이트
        self.sum += node.val
        node.val = self.sum
        # 왼쪽 서브트리 탐색
        if node.left:
            self.reverseInOrder(node.left)

