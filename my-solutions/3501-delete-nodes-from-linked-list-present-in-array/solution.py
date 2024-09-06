# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        
        dic = {}
        ans =[]
        for i in nums:
            if i not in dic:
                dic[i] = 1

        dummy = ListNode(0)
        current = dummy
        
        # 연결 리스트를 순회하며 dic에 있는 값만 새로운 리스트에 추가
        while head:
            if head.val not in dic:
                current.next = ListNode(head.val)
                current = current.next
            head = head.next
        
        # 새로 생성한 연결 리스트의 head 반환
        return dummy.next
        
        
