# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        nums = []
        while head:
            nums.append(head.val)
            if head.next:
                curr = head.next
                head = curr
            else:
                break
        ans = 0
        n = len(nums)
        start,end = 0 , n-1
        for i in range(n//2):
            if nums[start] + nums[end] > ans:
                ans = nums[start] + nums[end]
            start += 1
            end -= 1
        return ans
