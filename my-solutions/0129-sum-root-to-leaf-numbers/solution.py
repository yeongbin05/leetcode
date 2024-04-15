class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumNumbers(self, root):
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            # Update the current sum formed by appending the current node's value
            curr_sum = curr_sum * 10 + node.val
            
            # If it's a leaf node, return the current sum
            if not node.left and not node.right:
                return curr_sum
            
            # Recursively traverse left and right subtrees, adding their sums
            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
        
        return dfs(root, 0)
