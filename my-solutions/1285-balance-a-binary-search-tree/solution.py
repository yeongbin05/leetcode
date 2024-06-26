# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Step 1: Perform an in-order traversal to get the elements in sorted order
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        # Step 2: Build a balanced BST from the sorted elements
        def sorted_list_to_bst(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = sorted_list_to_bst(nums[:mid])
            root.right = sorted_list_to_bst(nums[mid+1:])
            return root
        
        # Get the sorted elements from the original BST
        sorted_values = inorder_traversal(root)
        # Build and return the balanced BST
        return sorted_list_to_bst(sorted_values)

