from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def kthLargestLevelSum(self, root, k):
        if not root:
            return 0
        
        # BFS로 각 레벨의 합을 계산
        level_sums = []
        queue = deque([root])
        
        while queue:
            level_sum = 0
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            level_sums.append(level_sum)
        
        # k번째로 큰 합을 찾기 위해 정렬 후 반환
        level_sums.sort(reverse=True)
        
        if k <= len(level_sums):
            return level_sums[k - 1]
        else:
            return -1  # k가 레벨의 수보다 클 경우

