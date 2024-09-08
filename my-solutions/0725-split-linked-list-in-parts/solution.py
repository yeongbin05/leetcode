# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def splitListToParts(self, head, k):
        # 연결 리스트의 길이를 계산합니다.
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # 각 부분의 기본 크기와 추가로 나누어질 크기를 계산합니다.
        part_size = length // k
        extra_parts = length % k
        
        # 결과를 저장할 리스트입니다.
        result = []
        current = head
        for i in range(k):
            part_head = current
            # 현재 부분의 크기를 결정합니다.
            current_part_size = part_size + (1 if i < extra_parts else 0)
            
            # 현재 부분을 잘라냅니다.
            for j in range(current_part_size - 1):
                if current:
                    current = current.next
            
            # 잘라낸 부분을 연결 리스트에서 분리합니다.
            if current:
                next_part = current.next
                current.next = None
                current = next_part
            
            # 결과에 추가합니다.
            result.append(part_head)
        
        return result

# 연결 리스트 생성
def create_linked_list(arr):
    head = ListNode(arr[0]) if arr else None
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# 예시 실행
solution = Solution()
head = create_linked_list([1, 2, 3])
k = 5
result = solution.splitListToParts(head, k)

# 결과 출력
for part in result:
    print_linked_list(part)

