# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_val = [0] * 10001
        ans,ans_level  = -float('inf'),0
        max_level = 0
        def recur(level,parent):
            nonlocal max_level
            if not parent:
                return
            level_val[level] += parent.val
            recur(level+1,parent.left)
            recur(level+1,parent.right)
            max_level = max(max_level,level)
        
        recur(1,root)
        for i in range(1,max_level+1):
            if level_val[i] > ans :
                ans = level_val[i]
                ans_level = i
        return ans_level
