# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def change(left,right,level):
            if not left or not right :
                return

            if level % 2 == 1:
                left.val,right.val = right.val,left.val
            
            change(left.left,right.right,level+1)
            change(left.right,right.left,level+1)

        if root:
            change(root.left,root.right,1)

        return root
