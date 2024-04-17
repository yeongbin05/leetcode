# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        def dfs(node, path):
            if not node:
                return
            
            # Convert node value to character
            char = chr(ord('a') + node.val)
            
            # Append the character to the path
            path.append(char)
            
            # If the node is a leaf, update the result
            if not node.left and not node.right:
                # Reverse the path to get the string from leaf to root
                current_str = ''.join(path[::-1])
                
                # Update the result if the current string is lexicographically smaller
                if not self.result or current_str < self.result:
                    self.result = current_str
            
            # Traverse left and right subtrees
            dfs(node.left, path)
            dfs(node.right, path)
            
            # Remove the last character when backtracking
            path.pop()

        self.result = ''
        dfs(root, [])
        return self.result
        
