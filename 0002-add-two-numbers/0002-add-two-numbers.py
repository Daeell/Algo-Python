# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr_node = head
        flag = 0
        while l1 or l2 or flag:
            val_one = l1.val if l1 else 0
            val_two = l2.val if l2 else 0
            tmp = val_one + val_two + flag
            flag = tmp // 10
            tmp = tmp % 10
            new_node = ListNode(tmp)
            curr_node.next = new_node
            curr_node = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return head.next

# 2개의 음수가 아닌 정수들을 나타내는 2개의 비어있지 않은 연결 리스트. 숫자는 역순으로 저장되며 각 노드에는 단일 숫자가 포함된다.
# 두 숫자를 더하고 합계를 링크된 목록으로 반환합니다.
# 두 숫자에는 숫자 0 자체를 제외하고 선행 0이 포함되어 있지 않다고 가정할 수 있습니다.

# 숫자 