# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flipEquiv(self, root1, root2):
        # 둘 다 None이면 True (같다는 뜻)
        if not root1 and not root2:
            return True
        # 둘 중 하나만 None이거나 값이 다르면 False
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        # 자식을 바꾸지 않고 비교하거나, 자식을 바꿔서 비교한 결과가 하나라도 True면 OK
        return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or \
               (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
