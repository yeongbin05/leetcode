# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # fast 포인터를 n+1번 이동 (dummy부터 시작하므로)
        for _ in range(n + 1):
            fast = fast.next
        
        # fast가 None에 도달할 때까지 fast와 slow를 동시에 이동
        while fast:
            fast = fast.next
            slow = slow.next
        
        # slow의 다음 노드가 제거 대상이 됨
        slow.next = slow.next.next
        return dummy.next
