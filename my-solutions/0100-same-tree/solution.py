# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def isSameTree(self, p, q):
        def dfs(p, q):
            # 둘 다 None이면 True (둘 다 리프 노드인 경우)
            if not p and not q:
                return True
            # 둘 중 하나만 None이면 False
            if not p or not q:
                return False
            # 값이 다르면 False
            if p.val != q.val:
                return False
            # 왼쪽과 오른쪽 자식을 재귀적으로 비교
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        
        # dfs 함수 호출
        return dfs(p, q)
