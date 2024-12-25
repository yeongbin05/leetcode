# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        dic = {}
        ans = []
        def bfs(node,depth):
            if not node:
                return
            if depth in dic:
                dic[depth] += [node.val]

            else :
                dic[depth] = [node.val]
                # print(dic)

            return bfs(node.left,depth+1), bfs(node.right,depth+1)
            

        bfs(root,1)
        for i in dic:
            ans.append(max(dic[i]))

        return ans
